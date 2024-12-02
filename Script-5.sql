CREATE TABLE clientes (
id_cliente serial PRIMARY KEY,
nome_cliente varchar(50) NOT NULL,
endereco text not NULL,
cpf char(11) NOT NULL,
telefone varchar(11) NOT null
);
create table produtos (
id_produto serial primary key,
nome_produto varchar(70) not null,
quantidade_produto int not null,
preco_produto real not null
);
create table compras (
id_compra serial primary key,
id_cliente int references clientes(id_cliente),
id_produto int references produtos(id_produto),
id_usuario int not null,
foreign key (id_usuario) references usuarios.usuarios(id),
preco_compra real not null
);
