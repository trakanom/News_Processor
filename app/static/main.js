$(document).ready(function () {
    // Initialize the Advanced Options display based on the checkbox state
    if ($("#advanced").is(":checked")) {
        $("#advanced_options").show();
    } else {
        $("#advanced_options").hide();
    }

    // Toggle the Advanced Options display when the checkbox state changes
    $("#advanced").change(function () {
        if ($(this).is(":checked")) {
            $("#advanced_options").show();
        } else {
            $("#advanced_options").hide();
        }
    });

    // Handle the View Results button click
    $(".view-results").click(function () {
        let news_data = JSON.parse($(this).data("results"));
        let results_container = $("ul.results");
        results_container.empty();
        news_data.forEach(article => {
            results_container.append(
                `<li><a href="${article.url}">${article.title}</a> - ${article.source.name}</li>`
            );
        });
    });
});
