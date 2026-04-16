#include "carro.h"

carro::carro(){
	marca = "Sin marca";
	modelo = 0;

carro::carro(string m, int mod){
	marca = m;
	modelo = mod;
}

void carro::imprimir(){
	cout<<"Marca: "<<marca<<endl;
	cout<<"Modelo: "<<modelo<<endl;
	cout<<endl;
}

void carro::setMarca(string m){
	marca = m;
}

string carro::getMarca(){
	return marca;
}

void carro::setModelo(int m){
	modelo = m;
}

int carro::getModelo(){
	return modelo;
}

void leer(carro v[], string archi){

	ifstream archivo(archi.c_str());

	for(int i=0;i<5;i++){
		string marca;
		int modelo;
		archivo>>marca>>modelo;
		v[i].setMarca(marca);
		v[i].setModelo(modelo);
	}

	archivo.close();
}

void mostrar(carro v[]){

	for(int i=0;i<5;i++){
		v[i].imprimir();
	}

}
void guardar(carro v[], string archi){

	ofstream archivo(archi.c_str());

	for(int i=0;i<5;i++){
		archivo<<v[i].getMarca()<<" "
			<<v[i].getModelo()<<endl;
	}

	archivo.close();
}
