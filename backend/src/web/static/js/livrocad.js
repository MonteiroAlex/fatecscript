var myApp = angular.module('myApp', [], function($interpolateProvider) {
	$interpolateProvider.startSymbol('{_');
	$interpolateProvider.endSymbol('_}');
});


function controller($scope, $http){

    $scope.livros = []
 	$http.get('/livrocad/listar').success(function (json){
 		$scope.livros = json;
 	})

  	$scope.editarLivro = function(livro){
  		livro.editando = true;
  	}

 	$scope.salvarLivro = function(){

 		var livro = {"autor":$scope.inputAutor,
 				    "titulo":$scope.inputTitulo,
 				   "editora":$scope.inputEditora,
 				   "paginas":$scope.inputPaginas};

 		$http.post('/livrocad/salvar', livro).success(function (json){

 			livro.idLivro = json.idLivro;
 			livro.editando = false;
 			$scope.livros.push(livro);

 			$scope.inputAutor = "";
 			$scope.inputTitulo = "";
 			$scope.inputEditora = "";
 			$scope.inputPaginas = "";

 		});

 	}

  	$scope.confirmarEdicao = function(livro){
  		livro.editando = false;

 		params =  {"idLivro":livro.idLivro,
 				     "autor":livro.autor,
 				    "titulo":livro.titulo,
 				   "editora":livro.editora,
 				   "paginas":livro.paginas}

 		$http.post('/livrocad/editar', params);
  	}

  	$scope.removerElemento = function(livro, index){
  		$scope.livros.splice(index, 1);
  		livro.editando = false;

 		$http.post('/livrocad/remover', {"idLivro":livro.idLivro});
  	}
}