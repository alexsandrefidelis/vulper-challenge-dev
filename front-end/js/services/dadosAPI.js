(function(){
	'use strict';
	angular
	.module('vulpersChallenge')
	
	.factory('dadoAPI', dadoAPI);
	
	dadoAPI.$inject = ['$http']
	
	function dadoAPI($http){
		var _info = function(dado){
			return $http.post('http://localhost:3000/dados/info', dado);
		};
		
		return{
			info:_info
		}
	}
	
	
})()