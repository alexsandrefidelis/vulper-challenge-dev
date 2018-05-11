(function(){
	'use strict';
	
	angular
	.module('vulpersChallenge')
	.controller('dadoController', dadoController);
	
	dadoController.$inject = ['dadoAPI','$scope'];
	
	function dadoController(dadoAPI,$scope){
		$scope.info = [];
		}
	}
})()