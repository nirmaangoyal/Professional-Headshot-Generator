document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('imageUpload');
    const fileName = document.getElementById('fileName');
    const generateButton = document.getElementById('generateButton');
    const loading = document.getElementById('loading');
    const resultImage = document.getElementById('resultImage');

    fileInput.addEventListener('change', function() {
        if (this.files && this.files[0]) {
            fileName.textContent = this.files[0].name;
        } else {
            fileName.textContent = 'No file chosen';
        }
    });

    generateButton.addEventListener('click', generateHeadshot);

    async function generateHeadshot() {
        const file = fileInput.files[0];
        if (!file) {
            alert('Please select an image file.');
            return;
        }

        loading.style.display = 'block';
        resultImage.style.display = 'none';

        const formData = new FormData();
        formData.append('image', file);

        try {
            const response = await fetch('/generate_headshot', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
            }

            const blob = await response.blob();
            const imageUrl = URL.createObjectURL(blob);
            resultImage.src = imageUrl;
            resultImage.style.display = 'block';
        } catch (error) {
            console.error('Error:', error);
            alert(`An error occurred while generating the headshot: ${error.message}`);
        } finally {
            loading.style.display = 'none';
        }
    }
});