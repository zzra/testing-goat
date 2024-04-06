window.Superlists = {};
window.Superlists.initialize = () => {
	const hideErrors = () => $('.errorlist').hide();

	$('input[name="text"]').on({
		'keypress': hideErrors, 
		'click': hideErrors
	});
};