//TODO: 
// 1. Fetch complaints from the backend
// 2. Display complaints in the table

function fetchComplaints() {
    fetch('http://localhost:3000/complaints')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            //displayComplaints(data);
        });
}

// Fake function to generate complaint data
function generateFakeComplaints() {
    return [
        {
            id: 1,
            time: '2023-10-01 14:30',
            class: 'Straßenschaden',
            category: 'Infrastruktur',
            image: 'https://via.placeholder.com/100'
        },
        {
            id: 2,
            time: '2023-10-02 09:15',
            class: 'Verschmutzung',
            category: 'Umwelt',
            image: 'https://via.placeholder.com/100'
        },
        {
            id: 3,
            time: '2023-10-03 16:45',
            class: 'Lärmbelästigung',
            category: 'Lärm',
            image: 'https://via.placeholder.com/100'
        }
    ];
}

$(document).ready(function() {
    fetchComplaints();

    var complaints = generateFakeComplaints();
    var tableBody = $('#complaintTableBody');

    complaints.forEach(function(complaint) {
        var row = '<tr>' +
            '<td>' + complaint.id + '</td>' +
            '<td>' + complaint.time + '</td>' +
            '<td>' + complaint.class + '</td>' +
            '<td>' + complaint.category + '</td>' +
            '<td><img src="' + complaint.image + '" alt="Complaint Image"></td>' +
            '</tr>';
        tableBody.append(row);
    });
});