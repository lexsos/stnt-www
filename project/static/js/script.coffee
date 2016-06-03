$ = jQuery
$(document).ready =>

  set_ajax_feedback = ->
        $('#feedback_response_form').ajaxForm
            success: (data) ->
                $('#feedback-dialog').html data
                set_ajax_feedback()
            beforeSubmit: ->
                $('#feedback_response_form .send-progress').css('display', 'inline')
                true
  set_ajax_feedback()

  set_ajax_connect_request = ->
        $('#connect_request_form').ajaxForm
            success: (data) ->
                $('#tariff-connect-dialog').html data
                set_ajax_connect_request()
            beforeSubmit: ->
                $('#connect_request_form .send-progress').css('display', 'inline')
                true
  set_ajax_connect_request()

  $('.tariff-thumbnail').click ->
    tariffId = $(this).attr('tatiff_id')
    $('#tariff-connect-dialog #id_tariff').val(tariffId)