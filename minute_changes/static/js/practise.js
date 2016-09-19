var timer = new Timer();
var timerStarted = false;

$('#timer .values').html(timer.getTimeValues().toString());
timer.addEventListener('secondsUpdated', function (e) {
    // there is a pre-timer that counts down before the actual timer starts
    // so that the user has time to pick up the guitar etc.
    console.log(timerStarted)
    if (timerStarted) {
      $('#timer .prefix').html('Stop in: ');
    } else {
      $('#timer .prefix').html('Start in: ');
    }
    $('#timer .values .minutes').html(timer.getTimeValues().minutes);
    $('#timer .values .seconds').html(timer.getTimeValues().seconds);
});

timer.addEventListener('stopped', function (e) {
  if (timerStarted) {
    // timer was running, so now stop
    $('#timer .values').html('STOP!!');
    $('#changes-submit').prop('disabled', false);
  } else {
    // pre-timer was running. Start the actual timer now
    timer.start({countdown: true, startValues: {seconds: 60}, precision: 'seconds'});
    console.log(timer.isRunning())
    $('#timer .values .minutes').html("0");
    $('#timer .values .seconds').html("60");
    timerStarted = true;
  }
});

$(document).ready(function() {
  $("#start-btn").click(function(event) {
    timer.start({countdown: true, startValues: {seconds: 3}, precision: 'seconds'});
    timerStarted = false;
    $('#start-btn').prop('disabled', true);
  })
});
