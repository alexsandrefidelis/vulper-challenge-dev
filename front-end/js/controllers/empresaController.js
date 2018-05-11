(function(){
	'use strict';
	
	angular
	.module('vulpersChallenge')
	.controller('empresaController', empresaController);
	
	empresaController.$inject=['empresaAPI','$scope'];
	
	function empresaController(empresaAPI,$scope){
		$scope.empresas = [];
		
		$scope.listar = function(){
			empresaAPI.listar().success(function(data){
				$scope.empresas = data;
			});
		}
	}
})();