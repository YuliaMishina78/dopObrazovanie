/**
 * Created by Yulia on 22-May-16.
 */
$(function () {
    $("#slider-range").slider({
        range: true,
        min: 300,
        max: 3000,
        values: [500, 1000],
        slide: function (event, ui) {
            $("#price-from").val(ui.values[0]);
            $("#price-to").val(ui.values[1]);
        }
    });

    /// Вывод в текстовое поле
    /*$("#amount").val("" + $("#slider-range").slider("values", 0) +
     " - " + $("#slider-range").slider("values", 1));*/

    $("#price-from").keyup(function () {
        $("#slider-range").slider("values", 0, $("#price-from").val());
    });

    $("#price-to").keyup(function () {
        $("#slider-range").slider("values", 1, $("#price-to").val());
    });
});