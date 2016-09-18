var timer = new Timer();
$('#timer .values').html(timer.getTimeValues().toString());
timer.addEventListener('secondsUpdated', function (e) {
    $('#timer .values .minutes').html(timer.getTimeValues().minutes);
    $('#timer .values .seconds').html(timer.getTimeValues().seconds);
});
timer.addEventListener('targetAchieved', function (e) {
    $('#timer .values').html('STOP!!');
    $('#changes-submit').prop('disabled', false)
});

$(document).ready(function() {
  $("#start-btn").click(function(event) {
    timer.start({countdown: true, startValues: {seconds: 5}, precision: 'seconds'});
  })
});
