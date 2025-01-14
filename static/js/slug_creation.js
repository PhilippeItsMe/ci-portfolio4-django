document.addEventListener('DOMContentLoaded', function () {
    const firmInput = document.getElementById('firm-input');
    const slugInput = document.getElementById('slug-input');

    firmInput.addEventListener('input', function () {
        const slugified = firmInput.value
            .toLowerCase()
            .replace(/[^a-z0-9]+/g, '-') // Replace non-alphanumeric characters with dashes
            .replace(/^-+|-+$/g, ''); // Remove leading/trailing dashes
        slugInput.value = slugified;
    });
});