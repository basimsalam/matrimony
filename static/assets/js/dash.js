const ctx = document.getElementById('dashboardChart').getContext('2d');
const dashboardChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Users', 'Premium Users', 'Success Rate', 'Inactive Users'],
        datasets: [{
            label: 'Statistics',
            data: [500, 300, 85, 150], // Example data
            backgroundColor: [
                'rgba(0, 0, 139, 0.5)',
                'rgba(0, 100, 0, 0.2)',
                'rgba(128, 0, 128, 0.2)',
                'rgba(255, 99, 132, 0.2)'
            ],
            borderColor: [
                'rgba(75, 192, 192, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(255, 99, 132, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
