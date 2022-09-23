
console.log("I'm here");
$(document).ready(function(){
	
	var content = "";

	$.each(data, function(){
		content = content + "<div class='col-md-3'><h2>" + this.pagetitle + "</h2><h3>Descriptions</h3>";
		$.each(this.DescAccordions, function(){
			content = content + "<a href=\"" + this.ID + ".html\" target='_blank'>" + this.accordiontitle + "</a><br>";	
		});
		content = content + "<h3>Tasks</h3>"
		$.each(this.TaskAccordions, function(){
			content = content + "<a href=\"" + this.ID + ".html\" target='_blank'>" + this.accordiontitle + "</a><br>";	
		});
		content = content + "<h3>" + this.pagetitle + " Videos</h3>"
		content = content + "</div>"


	})
	$('#links').html(content);
	});