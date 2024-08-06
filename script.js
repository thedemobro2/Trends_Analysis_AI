async function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (!file) {
        alert('Please select a file.');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    // Replace with your API endpoint to process the file and get trends analysis
    const apiEndpoint = 'https://your-api-endpoint.com/analyze';

    try {
        const response = await fetch(apiEndpoint, {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        document.getElementById('results').innerText = JSON.stringify(result, null, 2);
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to analyze the file.');
    }
}
