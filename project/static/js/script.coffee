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