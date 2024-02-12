document.getElementById('select-image-btn').addEventListener('click', function() {
    document.getElementById('image-input').click();
});

document.getElementById('image-input').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        // Display the file name
        const imageNameElement = document.getElementById('image-name');
        imageNameElement.textContent = `Selected: ${file.name}`;
        imageNameElement.classList.add('visible');
        
        // Optionally, display the image preview
        const reader = new FileReader();
        reader.onload = function(e) {
            const dogImageElement = document.getElementById('dog-image');
            dogImageElement.src = e.target.result;
            dogImageElement.classList.add('visible');
        };
        reader.readAsDataURL(file);
    }
});

document.getElementById('upload-image-btn').addEventListener('click', function() {
    const input = document.getElementById('image-input');
    if (!input.files.length) {
        alert('Please select an image first.');
        return;
    }

    // Show a loading message
    const uploadStatusElement = document.getElementById('upload-status');
    uploadStatusElement.textContent = 'Uploading...';
    uploadStatusElement.classList.add('visible');

    const formData = new FormData();
    formData.append('dogImage', input.files[0]);
    
    fetch('/upload', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        // Display the result
        const breedNameElement = document.getElementById('breed-name');
        const predictionTextElement = document.getElementById('prediction-text');
        const predictionResultElement = document.getElementById('prediction-result');

        breedNameElement.textContent = data.breed;
        predictionTextElement.textContent = `This dog is ${data.probability}% likely to be a ${data.breed}.`;
        predictionResultElement.classList.add('visible');

        // Hide the loading message
        uploadStatusElement.classList.remove('visible');
    })
    .catch(error => {
        console.error('Error:', error);
        uploadStatusElement.textContent = 'Upload failed. Try again.';
        // No need to remove the visible class here since we want to show the error
    });
});
