(function(){
	'use strict';
	
	angular
	.module('vulpersChallenge')
	.factory('empresaAPI',empresaAPI);
	
	empresaAPI.$inject = ['$http'];
	
	function empresaAPI($http){
		var _listar  = function(){
			return $http.get('http://localhost:3000/empresas/');
		};
		
		return{
			listar:_listar
		}
	}
})()
