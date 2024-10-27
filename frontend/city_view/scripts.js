// TODO:
// 1. Complaints anzeigen
// 2. Bilder anzeigen

$(document).ready(function() {
    fetchComplaints();
});

function fetchComplaints() {
    $.ajax({
        url: 'http://localhost:8000/smartcomplaint/complaint', // Verwende den korrekten API-Endpunkt
        method: 'GET',
        success: function(data) {
            var tableBody = $('#complaintTableBody');
            tableBody.empty(); // Clear existing rows

            data.forEach(function(complaint) {
                var imageUrl = 'http://localhost:8000/smartcomplaint/image/' + complaint.id;
                var row = '<tr>' +
                    '<td>' + complaint.id + '</td>' +
                    '<td>' + complaint.capture_time + '</td>' +
                    '<td>' + complaint.image_class + '</td>' +
                    '<td>' + complaint.category + '</td>' +
                    '<td><img src="' + imageUrl + '" alt="Complaint Image" style="max-width: 100px; max-height: 100px;"></td>' +
                    '</tr>';
                tableBody.append(row);
            });
        },
        error: function(error) {
            console.error('Error fetching complaints:', error);
        }
    });
}