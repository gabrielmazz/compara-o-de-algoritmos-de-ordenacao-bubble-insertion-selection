#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int* listArq(FILE* file, int size) {
    int* lista;
    int count = 0;
    lista = (int*)malloc(size * sizeof(int));
    int lec;
    while (fscanf(file, "%d", &lec) != EOF) {
        lista[count] = lec;
        count++;
    }
    return lista;
}

int main() {
    int indices[] = {100, 200, 500, 1000, 2000, 5000, 7500, 10000, 15000, 30000, 50000, 75000, 100000, 200000, 500000, 750000, 1000000, 1250000, 1500000, 2000000};
    //int indices[] = {100, 1000, 10000};
    int numIndices = sizeof(indices) / sizeof(indices[0]);
    FILE* result = fopen("resultadosBubble.txt", "w");

    double start, end, time_taken;

    for (int i = 0; i < numIndices; i++) {
        char nameOrd[40];
        char nameDec[40];
        char namePar[45];
        char nameAle[40];
        sprintf(nameOrd, "Ordenados/o%d.txt", indices[i]);
        sprintf(nameDec, "Decrescentes/d%d.txt", indices[i]);
        sprintf(namePar, "ParcialmenteOrdenados/po%d.txt", indices[i]);
        sprintf(nameAle, "Aleatórios/a%d.txt", indices[i]);

        FILE* fo = fopen(nameOrd, "r");
        int olSize = indices[i];
        int* ol = listArq(fo, olSize);
        fclose(fo);

        FILE* fd = fopen(nameDec, "r");
        int dlSize = indices[i];
        int* dl = listArq(fd, dlSize);
        fclose(fd);

        FILE* fp = fopen(namePar, "r");
        int plSize = indices[i];
        int* pl = listArq(fp, plSize);
        fclose(fp);

        FILE* fa = fopen(nameAle, "r");
        int alSize = indices[i];
        int* al = listArq(fa, alSize);
        fclose(fa);

        printf("\nRodando para %d itens\n", indices[i]);
        fprintf(result, "Rodando para %d itens\n", indices[i]);
        
        start = clock();
        bubbleSort(ol, olSize);
        end = clock();
        time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
        printf("Tempo de Bubble Sort para Ordenado com %d itens: %f\n", indices[i], time_taken);
        fprintf(result, "Tempo de Bubble Sort para Ordenado com %d itens: %f\n", indices[i], time_taken);
        
        start = clock();
        bubbleSort(dl, dlSize);
        end = clock();
        time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
        printf("Tempo de Bubble Sort para Decrescente com %d itens: %f\n", indices[i], time_taken);
        fprintf(result, "Tempo de Bubble Sort para Decrescente com %d itens: %f\n", indices[i], time_taken);
        
        start = clock();
        bubbleSort(pl, plSize);
        end = clock();
        time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
        printf("Tempo de Bubble Sort para Parcialmente Ordenado com %d itens: %f\n", indices[i], time_taken);
        fprintf(result, "Tempo de Bubble Sort para Parcialmente Ordenado com %d itens: %f\n", indices[i], time_taken);

        start = clock();
        bubbleSort(al, alSize);
        end = clock();
        time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
        printf("Tempo de Bubble Sort para Aleatório com %d itens: %f\n", indices[i], time_taken);
        fprintf(result, "Tempo de Bubble Sort para Aleatorio com %d itens: %f\n", indices[i], time_taken);
        
        fprintf(result, "\n=-=-=-=-=-=-=-=-=-=\n\n");
        
        free(ol);
        free(dl);
        free(pl);
        free(al);
    }
    fclose(result);
    return 0;
}