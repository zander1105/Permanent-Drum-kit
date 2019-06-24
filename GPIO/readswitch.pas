Program ReadSwitch;

Uses sysutils, baseunix;

var t1, t2, tstart, second : TDateTime;

var  pin_direction, pin_edge : text;
var pin_value : file;
var x1, x2    : char;

Begin
//   Writeln ('The time is : ',TimeToStr(Now));
//   writeln (t1);

   t1 := time;
   sleep(1000);
   t2 := time;
   second := t2 - t1;    {Time ticks in one second. }

   assign (pin_direction, '/sys/class/gpio/gpio23/direction');
   assign (pin_value,      '/sys/class/gpio/gpio23/value');
   assign (pin_edge,      '/sys/class/gpio/gpio23/edge');
   
   rewrite(pin_direction);
   rewrite(pin_edge);
   reset(pin_value, 1);

   write(pin_direction, 'in');
   close(pin_direction);
//   write(pin_edge, 'both');
//   close(pin_edge);

   t1 := Time;
   tstart := t1;
   blockread(pin_value,x1,1);
   seek(pin_value, 0);
   while TRUE do
   begin
      blockread(pin_value,x2,1);
      seek(pin_value, 0);      
      if x1 <> x2 then
      begin
	 t2 := Time;
	 writeln((t2 - tstart) / second : 15:6 , '  ', x1, ' for ', (t2 - t1) / second :15:6 );
	 x1 := x2;
	 t1 := t2;
      end
   end
End.
