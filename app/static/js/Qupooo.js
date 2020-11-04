//var query_lname=[];
//var query_salary=[];

$(document).ready(function(){
var query_lname=[];
var query_salary=[];
/*if (i == 3){
  await sleep(2000);
}*/

function doTheThing() {
  $.ajax({
    url: '/data',
    type: 'GET',
    dataType: "json",
  })
  .done(function (data) {
    for (var i = 0; i < data.length; i++ ) {
      query_lname.push(data[i].last_name);
      query_salary.push(data[i].salary);
    }
    console.log('Hello from doTheThing()')
  })
  .done(function (data) {
    console.log(query_lname)
    console.log('5330')
    console.log('Hello again')
    var ctx = document.getElementById('myChart');

    var data = {
      labels: query_lname,
      datasets: [{
        label: "Dataset #1",
        backgroundColor: "rgba(255,99,132,0.2)",
        borderColor: "rgba(255,99,132,1)",
        borderWidth: 2,
        hoverBackgroundColor: "rgba(255,99,132,0.4)",
        hoverBorderColor: "rgba(255,99,132,1)",
        data: query_salary,
      }]
    };

    var option = {
      responsive: false,
      scales: {
        yAxes: [{
          stacked: true,
          gridLines: {
            display: true,
            color: "rgba(255,99,132,0.2)"
          }
        }],
        xAxes: [{
          gridLines: {
            display: false
          }
        }]
      }
    };

    var myChart = new Chart(ctx, {
      type: 'bar',
      options: option,
      data: data
    });
  })
  .fail(function (error) {
      console.log(error)
  });
}
doTheThing()


function loadData(){
  //return new Promise((resolve, reject) => {
    $.getJSON('/data', function(data, status, xhr){
      for (var i = 0; i < data.length; i++ ) {
        query_lname.push(data[i].last_name);
        query_salary.push(data[i].salary);
      }
    });
  //});
}

loadData()
/*
console.log(query_lname);
console.log(query_lname.length);
console.log(typeof query_lname)
console.log(Array.isArray(query_lname));
console.log(query_lname[0]);
console.log(typeof query_lname[0])
*/

});



//test_func({{ query|safe }});

/*

$(document).ready(function() {
  console.log('Hello from document ready!');
  {% for person in query %}
      console.log('{{ person.first_name }}');
      //buildChart('#sensor_chart_{{ sensor.id }}',
      //["{{ sensor.readings|join('\",\"', attribute='time')|safe }}"],
      //[{{ sensor.readings|join(',', attribute='hum_value') }}],
      //[{{ sensor.readings|join(',', attribute='temp_value') }}]);
  {% endfor %}
});

function test_func(query) {
  console.log(query)
        //var = query_labels;
        //for (var i = 0; i < arr.length; i++) {
          //console.log(arr[i]);
//}
};

$(document).ready(function(){
    $.ajax({
        type: "GET",
        url: "http://myserver:5000/sunshine",
        //dataType: 'json',
        success: function(data) {
            console.log("This is the returned data: " + JSON.stringify(data));
        },
        error: function(error){
            console.log("Here is the error res: " + JSON.stringify(error));
        }
    });
});

*/
