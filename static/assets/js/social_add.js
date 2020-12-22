jQuery(function ($) {

    $('#add-social').click(function () {
        var div = $(this).parent().siblings().remove($(this).parent()).clone()
        div.find('select').removeAttr('required');
        div.find('input').val('');
        var link_val = $(this).parent().siblings().find('option:selected').val();
        console.log(link_val)
        div.find(`option[value=${link_val}]`).remove();

        div.find('input').removeAttr('required')

        $(this).parent().parent().append(div);

        $(this).remove();
        console.log("NARMIN")
    })
    $.mask.definitions['9'] = '';
    $.mask.definitions['d'] = '[0-9]';
    $("input[name='company_phone']").mask("+994(dd) ddd dd dd");
    $("input[name='phone']").mask("+994(dd) ddd dd dd");

});