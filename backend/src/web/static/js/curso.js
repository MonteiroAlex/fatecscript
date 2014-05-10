
function MyAppCtrl($scope) {
    $scope.listaDeCursos = [
        {'detalhar_path': '/', 'nome': 'PyPrático'}
     ];
 function MyAppCtrl($scope, $http) {
    $scope.listaDeCursos = [];
    $http.get('/curso/rest/listar_cursos').success(function (lista) {
         $scope.listaDeCursos = lista;
     });

     $scope.editarCurso = function (curso) {
         curso.mostrandoInterfaceEdicao = false;
     };


     $scope.deletarCurso = function (curso, index) {
         $scope.listaDeCursos.splice(index, 1);

     };

      $scope.adicionarCurso = function () {
          var curso = {'nome': $scope.nomeDoCurso,
             'detalhar_path': '/',
              'descricao': $scope.descricaoDoCurso
          };
         $scope.listaDeCursos.push(curso);
         $scope.nomeDoCurso='';
         $scope.descricaoDoCurso='';
         $http.post('/curso/rest/salvar_curso', curso).success(function (obj) {
             curso.id=obj.id;
             curso.mostrandoInterfaceEdicao=false;
             $scope.listaDeCursos.unshift(curso);
             $scope.nomeDoCurso = '';
             $scope.descricaoDoCurso = '';

         })


      }

 }

}