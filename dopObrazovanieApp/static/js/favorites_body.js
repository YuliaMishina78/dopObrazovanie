/**
 * Created by Yulia on 22-May-16.
 */
function delete_from_favorites(id) {
    $.ajax({
        type: 'POST',
        url: '/',
        data: {
            "TeacherID": id,
            "csrfmiddlewaretoken": csrf,
            "operationType": "delete"
        },
        success: function (data) {
            if (data.status == 0) {
                $.get("favorites", function (data, status) {
                    $('#favorites').html($('#favorites', data).html());
                });
            }
        },
        error: function (xhr, status, err) {
        },
        complete: function (xhr, status) {
        }
    });
}

$(document).ready(function () {
    function getCookie(c_name) {
        if (document.cookie.length > 0) {
            c_start = document.cookie.indexOf(c_name + "=");
            if (c_start != -1) {
                c_start = c_start + c_name.length + 1;
                c_end = document.cookie.indexOf(";", c_start);
                if (c_end == -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start, c_end));
            }
        }
        return "";
    }

    $(function () {
        $.ajaxSetup({
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            }
        });
    });
});