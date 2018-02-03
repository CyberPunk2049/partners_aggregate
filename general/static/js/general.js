$( document ).ready(function() {
	
	var links=$('.partners-elem').map(function(el){ 
			return Number(this.id);
		}).get();
	
	if (window.location.pathname=="/"){
		if ($('.banklist-elem').length>0) {
					
			$('.banklist-elem').eq(0).addClass('banklist-on-elem');
			console.log($('.banklist-elem'))
			$.ajax({
				type:'GET',
				data:{
					id:$('.banklist-elem').eq(0).attr('id'),
					storesid:JSON.stringify(links)
				},
				success:function(data) {
					bank_partners(data);
				}
			});
			
			$('.banklist-elem').click(function() {
				var elem_id=$(this).attr('id');
				$('.banklist-elem').removeClass('banklist-on-elem');
				$(this).addClass('banklist-on-elem');
				$.ajax({
					type:'GET',
					data:{
						id:elem_id,
						storesid:JSON.stringify(links)
					},
					success:function(data) {
						bank_partners(data);
					}
				})
			});
		}
		
		$('#change-partners-elem').click(function() {
			$('#change-partners-form').submit();
		});
			
		$('#change-partners-form').bind('submit', function(eventObject) {
			var links=$('.partners-elem').map(function(el){ 
				return Number(this.id);
			}).get();
			$('#storesid').val(JSON.stringify(links));
			console.log($('#storesid'));
		});
	
	} else if (window.location.pathname=="/partners_selector/") {
		console.log("/partners_selector/");
		
		$('.selector-partners-elem').click(function() {
			$(this).toggleClass('selector-partners-elem-on');
		});
		
		$('#selector-partners-save').click(function() {
			$('#selector-partners-form').submit();
		});
		
		$('#selector-partners-form').bind('submit', function(eventObject) {
			var links=$('.selector-partners-elem-on').map(function(el){ 
				return Number(this.id);
			}).get();
			$('#storesid').val(JSON.stringify(links));
			console.log($('#storesid'));
		});
	
	}
	
});

function bank_partners(data) {
	console.log(data);
	$('.partners-elem').removeClass('partners-on-elem');
	var i=0;
	while (i<data.length){
		$('.right-box #'+data[i].toString()).addClass('partners-on-elem');
		i++;
	}
}