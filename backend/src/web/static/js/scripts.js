function salvarmaterial() {
    if (!verificarErros()) {
        $.ajax({
            url: '/material/negocio/salvar_material',
            type: 'POST',
            data: $('#form_material').serialize(),
            success: function() {
                alert('Material cadastrado com sucesso')
                window.location.href = '/material/negocio/cadastrar_material'
            }
        })
    }
}


function verificarErros() {
    var msg = ''
    $('.required').each(function() {
        if ($(this).val() == '') {
            var labelText = $(this).prev().text()
            msg = msg + labelText.substr(0, labelText.length - 1) + ' é obrigatório. <p />'
        }
    })
    if (msg != '') {
        $('.view').removeClass('hide')
        $('#msg_error').html(msg)
        return true
    }
    return false
}