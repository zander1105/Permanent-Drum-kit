Program PollSwitch1;
{ Program to display changes read from Raspberry Pi GPIO pin 23.
Uses the efficient linux poll facility, instead of wasteful read loop.}

Uses sysutils, baseunix;


var t1, t2, tstart, second : TDateTime;
   pin_direction, pin_edge : text;
   fd			   : THandle;
   x1, x2		   : char;
   poll_count		   : integer;
   po			   : tpollfd;

procedure read_pin_value (fd : THandle; var buf : char);
begin
   if FileRead(fd, buf, 1) < 1 then Halt(2);
   FileSeek(fd, 0, fsFromBeginning);
end;
   

Begin
   t1 := time;
   sleep(1000);
   t2 := time;
   second := t2 - t1;    {Time ticks in one second. }

   assign (pin_direction, '/sys/class/gpio/gpio23/direction');
   assign (pin_edge,      '/sys/class/gpio/gpio23/edge');

   fd := FileOpen('/sys/class/gpio/gpio23/value', fmOpenReadWrite);
   if fd < 0 then  begin
      writeln('Failed to open pin value file.');
      Halt(1);
   end;
   
   po.fd := fd;     {Initialize the poll structure for interrupt event.}
   po.events := POLLPRI;
   po.revents := 0;
   
   rewrite(pin_direction);
   rewrite(pin_edge);

   write(pin_direction, 'in');
   close(pin_direction);
   write(pin_edge, 'both');
   close(pin_edge);

   t1 := Time;
   tstart := t1;
   read_pin_value(fd, x1);
   writeln('Initial value is ', x1);
   poll_count := 0;
   
   while TRUE do
   begin
      poll_count := poll_count + 1;
      if FpPoll(@po, 1, 10000) > 0  { Event occurred. }
	 then begin
	    sleep(10);              { Wait 10 milliseconds for contact bounce. }
	    read_pin_value(fd, x2);
	    if x1 <> x2 then
	    begin
	       t2 := Time;
	       writeln((t2 - tstart) / second : 15:6 , '  ', x1, ' for ', (t2 - t1) / second :15:6, '   poll count=', poll_count );
	       x1 := x2;
	       t1 := t2;
	    end
	 end
	 else    { Time out - no event occurred. }
	    writeln('poll returned zero.');
   end
End.
