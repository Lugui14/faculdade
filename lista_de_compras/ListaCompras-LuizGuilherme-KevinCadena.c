/*
 Este é um esqueleto que deve ser utilizado como base para implementação do trabalho;
	- As funções não têm os parâmetros definidos; se necessário, estes devem ser incluídos; Os tipos de retorno podem ser alterados, se necessário;
 	- Devem ser respeitados os nomes atribuídos às funções e estruturas, porém, novas estruturas e funções podem ser criadas, caso julgue necessário;
	- Faça os includes necessários;
	- A organização das funções fica a critério do programador;
	- A indentação correta faz parte da nota;
	- Não são permitidas variáveis globais;
	- Caso seja detectado plágio, os grupos envolvidos receberão nota 0.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>
#include <ctype.h>

#define EXIT 10  // valor fixo para a opção que finaliza a aplicação

// Struct que representa um item de uma lista de compras armazenada em uma arvore binaria de busca
struct item {
    char produto[50];
    int quantidade;
    struct item  *esquerdo;
    struct item  *direito;
};
typedef struct item Item;

// Struct que representa um item da lista encadeada a ser exibida na intersecção
typedef struct itemEncadeado {
    char produto[50];
    struct itemEncadeado *proximo;
} ItemEncadeado;

//-------------------------------------------------------------------------------------------//

//Função para validar números inteiros
int inteiro()
{

    //variável que vai receber o suposto numero
    char entrada[100];

    //ponteiro para a 'string'
    gets(entrada);
    fflush(stdin);

    //looping para percorrer a string
    for (int i = 0; i < strlen(entrada); i++) {
        //verificação para ver se o caractere é um número decimal
        if (isdigit(entrada[i])) {
            //se for digito
            continue;
        } else {
            //se não for decimal retorna NULL
            return -5;
        }
    }

    return atof(entrada);
}

//-------------------------------------------------------------------------------------------//

// Apresenta o primeiro menu da aplicação e retorna a opção selecionada
int menu1()
{
    int op = 0;
    printf("\nMenu principal\n");

    printf("[1] - Gerenciar lista de compras A;\n");
    printf("[2] - Gerenciar lista de compras B;\n");
    printf("[3] - Visualizar itens duplicados.\n");

    printf("[%d] - Sair do programa", EXIT);
    printf("\nDigite a opcao:  ");

    //substituí o scanf para evitar erros no programa
    op = inteiro();

    //scanf("%d",&op);
    return op;
}

// Apresenta o segundo menu da aplicação e retorna a opção selecionada
int menu2()
{
    int op = 0;
    printf("\nSubmenu - Gerenciar lista de compras\n");

    printf("[1] - Inserir item na lista de compras;\n");
    printf("[2] - Pesquisar um produto na lista de compras;\n");
    printf("[3] - Atualizar a quantidade de um produto na lista de compras;\n");
    printf("[4] - Listar todos os itens da lista de compras em ordem alfabetica;\n");
    printf("[5] - Deletar item da lista de compras.\n");

    printf("[%d] - Retornar para o menu principal",EXIT);
    printf("\nDigite a opcao:  ");

    //substituí o scanf para evitar erros no programa
    op = inteiro();

    //scanf("%d",&op);
    return op;
}

//-------------------------------------------------------------------------------------------//

//função criada para fazer uma busca recursiva de um item específico
Item *search(Item **raiz, char produto[50]) {

    //se a arvore nao existir ou o produto nao existir
    if (*raiz == NULL) {
        return NULL;
    }

    //retorna o produto quando for achado na arvore
    if (strcmp(produto, (*raiz)->produto) == 0) {
        return (*raiz);
    }

    //percorre a arvore recursivamente até achar
    if (strcmp(produto, (*raiz)->produto) < 0) {
        return search(&(*raiz)->esquerdo, produto);
    } else {
        return search(&(*raiz)->direito, produto);
    }
}

//-------------------------------------------------------------------------------------------//

Item *create_item(char produto[50], int quantidade)
{
    //aloca memoria e cria o item
    Item *aux = malloc(sizeof(Item));

    //atribui os valores do item criado
    strcpy(aux->produto, produto);
    aux->quantidade = quantidade;
    aux->esquerdo = NULL;
    aux->direito = NULL;

    return aux;
}

// Permite o cadastro de um item (caso o produto ainda não exista) em uma lista de compas
void insert_recursividade(Item **raiz, char produto[50], int quantidade)
{

    //insere o item de acordo com a recursividade, quando a raiz for nula é porque esta no nó folha
    if (*raiz == NULL) {
        *raiz = create_item(produto, quantidade);
        printf("\nItem inserido com sucesso.\n");
    } else {
        //compara alfabeticamente o item
        int comp = strcmp(produto, (*raiz)->produto);

        //se vier antes é inserido na esquerda
        if (comp < 0) {
            insert_recursividade(&(*raiz)->esquerdo, produto, quantidade);

         //se vier depois é inserido na direita
        } else if (comp > 0) {
            insert_recursividade(&(*raiz)->direito, produto, quantidade);

          //se ja existir da um aviso e finaliza a recursão
        } else {
            printf("Item já existe na árvore, atualizando quantidade.\n");
        }
    }

    return;
}

// Função utilizada para evitar erros na recursividades
void insert(Item **raiz)
{
    //declara variaveis
    char produto[50];
    int quantidade;

    //pega os dados
    printf("\nDigite o nome do produto a ser inserido: ");
    gets(produto);
    fflush(stdin);
    printf("\nDigite a quantidade do produto: ");
    quantidade = inteiro();

    while(quantidade == -5) {
        printf("\nDigite a quantidade do produto em valor DECIMAL: ");
        quantidade = inteiro();
    }

    insert_recursividade(raiz, produto, quantidade);
    return;
}

//-------------------------------------------------------------------------------------------//

// Realiza a consulta de um item específico na lista de compras e printa ele
void query(Item **raiz)
{

    //declara variaveis
    char produto[50];

    //pega os dados
    printf("\nDigite o nome do produto que quer procurar: ");
    gets(produto);

    //realiza a busca
    Item *item = search(raiz, produto);

    //se a arvore ou o produto não existirem cai aqui
    if(item == NULL) {
        printf("\nO item procurado não está presente nessa lista de compras.\n");
        return;
    }

    //printa
    printf("\n-------------------------------\n");
    printf("Produto: %s\n", produto);
    printf("Quantidade: %d", item->quantidade);
    printf("\n-------------------------------\n");

    return;
}

//-------------------------------------------------------------------------------------------//

// Permite a atualização da quantidade de um produto (caso exista) na lista de compras
void update_recursividade(Item **raiz, char produto[50], int nova_quantidade)
{

    //verifica se o produto existe na lista de compras ou se a arvore não existe
    if(search(raiz, produto) == NULL) {
        printf("\nO produto especificado não existe nessa lista de compras.\n");
        return;
    }

    //quando achar o produto altera a quantidade do produto
    if (strcmp(produto, (*raiz)->produto) == 0) {
        (*raiz)->quantidade = nova_quantidade;
        printf("\nQuantidade do produto atualizada.\n");
        return;
    }

    //percorre recursivamente até encontrar o item especificado
    if (strcmp(produto, (*raiz)->produto) < 0) {
        update_recursividade(&(*raiz)->esquerdo, produto, nova_quantidade);
    } else {
        update_recursividade(&(*raiz)->direito, produto, nova_quantidade);
    }
}

//funcao para evitar declaração de variavel global
void update(Item **raiz)
{
    //declara variaveis
    char produto[50];
    int quantidade;

    //pega os dados
    printf("\nDigite o nome do produto a ser atualizado: ");
    gets(produto);
    fflush(stdin);
    printf("\nDigite nova quantidade: ");
    quantidade = inteiro();

    while(quantidade == -5) {
        printf("\nDigite a quantidade do produto em valor DECIMAL: ");
        quantidade = inteiro();
    }

    update_recursividade(&(*raiz), produto, quantidade);

}

//-------------------------------------------------------------------------------------------//

//conta quantos itens tem na arvore
int count(Item **raiz)
{
    //se a raiz for nula então é 0
    if((*raiz) == NULL){
        return 0;
    }

    //metodo para fazer somatoria do total
    return 1 + count(&(*raiz)->esquerdo) + count(&(*raiz)->direito);
}

// Lista todos os itens usando recursão
void list_recursividade(Item **raiz)
{
    if (*raiz == NULL) {
        return;
    }
    list_recursividade(&(*raiz)->esquerdo);

    if((*raiz)->produto != -1) {
        printf("\nProduto: %s - Quantidade: %d", (*raiz)->produto, (*raiz)->quantidade);
    }

    list_recursividade(&(*raiz)->direito);
}

// Se a arvore estiver vazia printa, senao chama a recursão pra printar
void list(Item **raiz)
{

    if(*raiz == NULL) {
        printf("\n*Essa lista de compras está vazia, tente adicionar itens primeiro.*\n");
        return;
    }

    list_recursividade(&(*raiz));
    return;
}

//-------------------------------------------------------------------------------------------//

//função utilizada para encontrar o nó com menor valor na subárvore da direita
Item *find_min(Item **raiz)
{
    //percorre recursivamente até achar o item com menor valor
    if((*raiz)->esquerdo == NULL) {
        return *raiz;
    }
    return find_min(&(*raiz)->esquerdo);
}

// Permite excluir um item de uma lista de compras
void delete_recursividade(Item **raiz, char produto[50])
{
    //verifica se a arvore existe
    if(*raiz == NULL) {
        printf("\nA lista está vazia, adicione algum item antes de tentar deletar.\n");
        return;
    }

    //se o valor for menor ele vai para o lado esquerdo da arvore
    if (strcmp(produto, (*raiz)->produto) < 0) {
        delete_recursividade(&(*raiz)->esquerdo, produto);

        //se for maior vai para o lado direito
    } else if (strcmp(produto, (*raiz)->produto) > 0) {
        delete_recursividade(&(*raiz)->direito, produto);

        //quando o valor for achado cai aqui
    } else {
        //se não tiver nó filho a esquerda, o valor é substituido pelo nó da direita e libera o espaço
        if ((*raiz)->esquerdo == NULL) {
            Item *aux = (*raiz);
            (*raiz) = (*raiz)->direito;
            free(aux);

            //se não tiver nó filho a direita, o valor é substituido pelo nó da esquerda e libera o espaço
        } else if ((*raiz)->direito == NULL) {
            Item *aux = (*raiz);
            (*raiz) = (*raiz)->esquerdo;
            free(aux);

            //se tiver nó na esquerda e na direita, é chamada uma função para encontrar o menor valor a direita e substituir
            //apos substituir ele chama novamente a função de deletar excluir o nó substituido
        } else {
            Item *aux = find_min(&(*raiz)->direito);
            strcpy((*raiz)->produto,aux->produto);
            (*raiz)->quantidade = aux->quantidade;
            delete_recursividade(&(*raiz)->direito, aux->produto);
        }
    }

    return;
}

//função para evitar usar variaveis globais
void delete(Item **raiz)
{
    //declara variavel
    char produto[50];

    //coleta dados
    printf("\nDigite o nome do produto a ser deletado: ");
    gets(produto);

    delete_recursividade(raiz, produto);
    return;
}

//-------------------------------------------------------------------------------------------//

//cria um novo item para a lista encadeada
ItemEncadeado *create_item_encadeada(char produto[50])
{
    ItemEncadeado *aux = malloc(sizeof(ItemEncadeado));
    strcpy(aux->produto, produto);
    aux->proximo = NULL;

    return aux;
}

//função para inserir itens na lista encadeada de duplicidade
void insert_encadeada(ItemEncadeado *pai, ItemEncadeado **raiz, char produto[50])
{
    //se for chegou no final da recursão cria o item e insere
    if((*raiz) == NULL) {
        *raiz = create_item_encadeada(produto);

        //se tiver um item pai, o proximo do item pai sera o atual
        if(pai != NULL) {
            pai->proximo = *raiz;
        }

        return;
    }

    //realiza a recursao
    ItemEncadeado *aux = (*raiz)->proximo;
    insert_encadeada(*raiz, &aux, produto);

}

//função para auxiliar a intersecção, criando arrays com os componentes
void fill_array(Item **raiz, char aux[][50], int *i)
{

    //se a raiz passada for nula então executa a recursão
    if ((*raiz) == NULL) {
        return;
    }

    //metodor recursivo para percorrer a arvore
    fill_array(&(*raiz)->esquerdo, aux, i);
    strcpy(aux[*i], (*raiz)->produto);
    //utiliza-se o ponteiro do inteiro para continuar a somatoria mesmo com a saida da função
    (*i)++;
    fill_array(&(*raiz)->direito, aux, i);

}

//imprime a lista encadeada
void print_encadeada(ItemEncadeado **raiz) {
    for(ItemEncadeado *aux = *raiz; aux != NULL; aux = aux->proximo) {
        printf("Produto: %s\n", aux->produto);
    }
}

//destroi lista encadeada quando terminada a intersecção
void kill_list(ItemEncadeado **raiz)
{
    //termina a recursão
    if((*raiz) == NULL) {
        return;
    }

    //recursividade
    kill_list(&(*raiz)->proximo);
    //libera memoria
    free((*raiz));
}

//realiza a intersecção
void intersect(Item **raizA, Item **raizB)
{

    //inicializa a lista encadeada
    ItemEncadeado *lista = NULL;

    //se uma das listas for nula não é possivel fazer a intersecção
    if (raizA == NULL || raizB == NULL) {
        printf("\n A uma das listas de compra está vazia.");
        return;
    }

    //faz a contagem dos itens das arvores
    int sizeA = count(raizA);
    int sizeB = count(raizB);

    //cria um array para cada arvore para facilitar a intersecção
    char auxA[sizeA][50];
    char auxB[sizeB][50];

    //preenche os arrays com os itens da arvore
    int i = 0;
    fill_array(&(*raizA), auxA, &i);
    i = 0;
    fill_array(&(*raizB), auxB, &i);

    //insere os itens que forem duplicados na lista encadeada
    for(int countA = 0; countA < sizeA; countA++) {
        for(int countB = 0; countB < sizeB; countB++) {
            if(strcmp(auxA[countA], auxB[countB]) == 0) {
                insert_encadeada(NULL, &lista, auxA[countA]);
            }
        }
    }

    //printa os itens duplicados
    printf("\nDuplicados nas listas\n");
    print_encadeada(&lista);
    kill_list(&lista);
}

//-------------------------------------------------------------------------------------------//

// Programa principal
int main()
{
    int opcao1;
    int opcao2;
    Item *raizA = NULL;
    Item *raizB = NULL;

    //permite o uso de acentuação
    setlocale(LC_ALL, "");

    /*
    insert_recursividade(&raizA, "azeite", 1);
    insert_recursividade(&raizA, "leite", 2);
    insert_recursividade(&raizA, "coca-cola", 3);
    insert_recursividade(&raizA, "pao", 4);
    insert_recursividade(&raizA, "arroz", 5);
    insert_recursividade(&raizA, "feijao", 6);

    insert_recursividade(&raizB, "pao", 1);
    insert_recursividade(&raizB, "banana", 2);
    insert_recursividade(&raizB, "coca-cola", 2);
    insert_recursividade(&raizB, "melancia", 6);
    insert_recursividade(&raizB, "arroz", 2);
    insert_recursividade(&raizB, "feijao", 7);
    */

    opcao1 = 0;
    while (opcao1 != EXIT)
    {
        opcao1 = menu1();

        switch(opcao1)
        {
            case 1 : // gerenciar lista de compras A
                opcao2 = 0;
                while(opcao2 != EXIT){
                    printf("\n\n** Lista de Compras A **\n\n");
                    opcao2 = menu2();
                    switch(opcao2){ // operacoes sobre a arvore A
                        case 1 :
                            insert(&raizA);
                            break;
                        case 2 :
                            query(&raizA);
                            break;
                        case 3 :
                            update(&raizA);
                            break;
                        case 4 :
                            list(&raizA);
                            break;
                        case 5 :
                            delete(&raizA);
                    }
                }
                break;
            case 2 : // gerenciar lista de compras B
                opcao2 = 0;
                while(opcao2 != EXIT){
                    printf("\n\n** Lista de Compras B **\n\n");
                    opcao2 = menu2();
                    switch(opcao2){ // operacoes sobre a arvore B
                        case 1 :
                            insert(&raizB);
                            break;
                        case 2 :
                            query(&raizB);
                            break;
                        case 3 :
                            update(&raizB);
                            break;
                        case 4 :
                            list(&raizB);
                            break;
                        case 5 :
                            delete(&raizB);
                            printf("\nItem deletado com sucesso.\n");
                    }
                }
            case 3 : // Visualizar itens duplicados
                intersect(&raizA, &raizB);

        }
    }
    return 0;
}
