
        function preview_image(event) {
            var reader = new FileReader();
            reader.onload = function () {
                var output = document.getElementById('output_image');
                output.src = reader.result;
            }

            reader.readAsDataURL(event.target.files[0]);
        }

       


       $("document").ready(function() {
        var checkTcNum = function(value) {
          value = value.toString();
          var isEleven = /^[0-9]{11}$/.test(value);
          var totalX = 0;
          for (var i = 0; i < 10; i++) {
            totalX += Number(value.substr(i, 1));
          }
          var isRuleX = totalX % 10 == value.substr(10,1);
          var totalY1 = 0;
          var totalY2 = 0;
          for (var i = 0; i < 10; i+=2) {
            totalY1 += Number(value.substr(i, 1));
          }
          for (var i = 1; i < 10; i+=2) {
            totalY2 += Number(value.substr(i, 1));
          }
          var isRuleY = ((totalY1 * 7) - totalY2) % 10 == value.substr(9,0);
          return isEleven && isRuleX && isRuleY;
        };


        $('#id_ogrenciTc').on('keyup', function(event) {
          event.preventDefault();
          var isValid = checkTcNum($(this).val());
          console.log('isValid ' , isValid);
          if (isValid) {
            $('#ogrenciTc').text("[Tc Kimlik Numarası Doğru]").attr('style', 'color: #155724;background-color: #d4edda;border-color: #c3e6cb; margin-left:20px;');
          }
          else {
            $('#ogrenciTc').text("[Tc Kimlik Numarası Yanlış]").attr('style', 'color: #721c24;background-color: #f8d7da;border-color: #f5c6cb; margin-left:20px;');
          }
        });
		
		
		$('#id_veliTc').on('keyup', function(event) {
          event.preventDefault();
          var isValid = checkTcNum($(this).val());
          console.log('isValid ' , isValid);
          if (isValid) {
            $('#veliTc').text("[Tc Kimlik Numarası Doğru]").attr('style', 'color: #155724;background-color: #d4edda;border-color: #c3e6cb; margin-left:20px;');
          }
          else {
            $('#veliTc').text("[Tc Kimlik Numarası Yanlış]").attr('style', 'color: #721c24;background-color: #f8d7da;border-color: #f5c6cb; margin-left:20px;');
          }
        });
		
		
		$('#id_anneTc').on('keyup', function(event) {
          event.preventDefault();
          var isValid = checkTcNum($(this).val());
          console.log('isValid ' , isValid);
          if (isValid) {
            $('#anneTc').text("[Tc Kimlik Numarası Doğru]").attr('style', 'color: #155724;background-color: #d4edda;border-color: #c3e6cb; margin-left:20px;');
          }
          else {
            $('#anneTc').text("[Tc Kimlik Numarası Yanlış]").attr('style', 'color: #721c24;background-color: #f8d7da;border-color: #f5c6cb; margin-left:20px;');
          }
        });
		
		
		$('#id_babaTc').on('keyup', function(event) {
          event.preventDefault();
          var isValid = checkTcNum($(this).val());
          console.log('isValid ' , isValid);
          if (isValid) {
            $('#babaTc').text("[Tc Kimlik Numarası Doğru]").attr('style', 'color: #155724;background-color: #d4edda;border-color: #c3e6cb; margin-left:20px;');
          }
          else {
            $('#babaTc').text("[Tc Kimlik Numarası Yanlış]").attr('style', 'color: #721c24;background-color: #f8d7da;border-color: #f5c6cb; margin-left:20px;');
          }
        });
		
		$('#id_personelTc').on('keyup', function(event) {
          event.preventDefault();
          var isValid = checkTcNum($(this).val());
          console.log('isValid ' , isValid);
          if (isValid) {
            $('#personelTc').text("[Tc Kimlik Numarası Doğru]").attr('style', 'color: #155724;background-color: #d4edda;border-color: #c3e6cb; margin-left:20px;');
          }
          else {
            $('#personelTc').text("[Tc Kimlik Numarası Yanlış]").attr('style', 'color: #721c24;background-color: #f8d7da;border-color: #f5c6cb; margin-left:20px;');
          }
        });
		
		
		$('#id_servisTC').on('keyup', function(event) {
          event.preventDefault();
          var isValid = checkTcNum($(this).val());
          console.log('isValid ' , isValid);
          if (isValid) {
            $('#servisTc').text("[Tc Kimlik Numarası Doğru]").attr('style', 'color: #155724;background-color: #d4edda;border-color: #c3e6cb; margin-left:20px;');
          }
          else {
            $('#servisTc').text("[Tc Kimlik Numarası Yanlış]").attr('style', 'color: #721c24;background-color: #f8d7da;border-color: #f5c6cb; margin-left:20px;');
          }
        });
		
      }); 