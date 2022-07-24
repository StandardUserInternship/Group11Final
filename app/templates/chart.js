var canvas = document.getElementById('MyChart')
var context = canvas.getContent('2d');
new Chart(context, {
    type: 'bar',
    data: {
        labels: [
            'Gender',
            'Sunken'
        ],
        datasets: [
        {
            label: 'My data',
            data: [1, 3]
        }

        ]
    }
})

