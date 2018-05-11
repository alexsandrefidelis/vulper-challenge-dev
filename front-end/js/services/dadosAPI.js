
var myApp = angular.module('myApp').factory("userService", function (API_URL, $http) {
  
	  userService.List = function () {
		  var promise = $http({
			  method: 'GET',
			  url: API_URL.url + '/vulpi-api/'
		  })
			  .then(function (response) {
				  return response.data.content;
			  },
			  function (response) {
				  //error action
			  });
  
		  return promise;
	  };

	  userService.New = function (userData) {
		 
		  var promise = $http({
			  method: 'POST',
			  url: API_URL.url + '/api/v1/usuario',
			  data: userData
  
		  })
			  .then(function (response) {
				  return response.data;
			  },
			  function (response) {
				   //error action
			  });
  
		  return promise;
	  };  
	  return userService;
  });

myApp.controller('userCtrl', ['$scope', 'userService', function ($scope, userService) {  
   
	$scope.empresas = userService.List();
}]);