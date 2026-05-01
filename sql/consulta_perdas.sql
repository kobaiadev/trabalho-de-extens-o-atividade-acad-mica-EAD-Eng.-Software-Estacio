-- Script para criação da estrutura de dados no banco (PostgreSQL/MySQL)
-- Nome do Projeto: trabalho-de-extensao-EAD-Eng.-Software-Estacio

CREATE TABLE Perdas_Varejo (
    Loja VARCHAR(100),
    Ano INT,
    Mes VARCHAR(20),
    Perdas_Brt DECIMAL(10,2)
);

-- Consulta para validar os dados filtrados pelo script Python
-- Foco no CNPJ da unidade: 15.347.973/0001-79
SELECT 
    Loja, 
    Ano, 
    Mes, 
    SUM(Perdas_Brt) as Total_Mensal
FROM Perdas_Varejo
WHERE Ano >= 2024
GROUP BY Loja, Ano, Mes
ORDER BY Ano DESC, Total_Mensal DESC;