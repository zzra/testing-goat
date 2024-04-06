const initialize = () => {
	$('input[name="text"]').on('keypress', () => {
		$('.errorlist').hide();
	});
};