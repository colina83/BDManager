document.addEventListener('DOMContentLoaded', function () {
    var cleave = new Cleave('input[name="cost"]', {
        numeral: true,
        numeralThousandsGroupStyle: 'thousand'
    });

    document.getElementById("submitButton").addEventListener("click", function() {
        var form = document.getElementById("projectForm");
        var costInput = document.querySelector('input[name="cost"]');
        costInput.value = cleave.getRawValue(); // Get the unformatted value

        // Submit the form
        form.submit();
    });
});