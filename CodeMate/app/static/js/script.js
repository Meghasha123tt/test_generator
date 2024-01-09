// script.js

function processPDF() {
    // Display processing message
    $('#processingMessage').text('Processing PDF...');

    // Perform AJAX request to process PDF
    $.ajax({
        type: 'POST',
        url: '/process_pdf',
        data: new FormData($('#uploadForm')[0]),
        processData: false,
        contentType: false,
        success: function (response) {
            // Display success message
            $('#processingMessage').text(response.message);
        },
        error: function (error) {
            // Display error message
            $('#processingMessage').text('Error processing PDF.');
            console.error(error);
        }
    });
}

function generateTest() {
    // Perform AJAX request to generate test
    $.ajax({
        type: 'POST',
        url: '/generate_test',
        data: {/* Include user-specified parameters here */},
        success: function (response) {
            // Display generated test questions and answers
            displayTest(response.questions, response.answers);
        },
        error: function (error) {
            // Display error message
            console.error(error);
        }
    });
}

function displayTest(questions, answers) {
    // Display generated test questions and answers
    var testHTML = '<h2>Generated Test</h2>';
    for (var i = 0; i < questions.length; i++) {
        testHTML += '<p><strong>Q' + (i + 1) + ':</strong> ' + questions[i] + '<br><strong>A:</strong> ' + answers[i] + '</p>';
    }

    $('#generatedTest').html(testHTML);
}
