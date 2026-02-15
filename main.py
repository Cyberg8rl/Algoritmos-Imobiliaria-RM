import csv

class OrcamentoImobiliaria:
    def __init__(self, cliente_nome, tipo_imovel, quartos=1, tem_garagem=False, tem_criancas=True, parcelas_contrato=5):
        self.cliente = cliente_nome
        self.tipo_imovel = tipo_imovel.lower()
        self.quartos = quartos
        self.tem_garagem = tem_garagem
        self.tem_criancas = tem_criancas
        self.valor_contrato_total = 2000.00 # 
        self.parcelas_contrato = max(1, min(5, parcelas_contrato)) # Max 5x [cite: 20, 29]
        self.mensalidade_base = 0.0

    def calcular_aluguel(self):
        # Definição de valores base por tipo de imóvel [cite: 16, 17, 18, 19]
        if self.tipo_imovel == 'apartamento':
            self.mensalidade_base = 700.00
            if self.quartos >= 2: self.mensalidade_base += 200.00 # [cite: 24]
            if not self.tem_criancas: self.mensalidade_base *= 0.95 # Desconto 5% 
            if self.tem_garagem: self.mensalidade_base += 300.00 # 
        
        elif self.tipo_imovel == 'casa':
            self.mensalidade_base = 900.00
            if self.quartos >= 2: self.mensalidade_base += 250.00 # [cite: 25]
            if self.tem_garagem: self.mensalidade_base += 300.00 # 
            
        elif self.tipo_imovel == 'estudio':
            self.mensalidade_base = 1200.00
            # Regra específica do Estúdio para vagas [cite: 27]
            if self.tem_garagem:
                # O PDF diz: R$ 250 por 2 vagas + R$ 60 por vaga extra
                # Aqui simulamos 2 vagas iniciais inclusas no adicional de 250
                self.mensalidade_base += 250.00 

        return self.mensalidade_base

    def gerar_csv(self):
        valor_mensal_contrato = self.valor_contrato_total / self.parcelas_contrato
        filename = r"C:\Users\User\OneDrive\Área de Trabalho\orcamento_final.csv"
        
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Mes', 'Aluguel Mensal', 'Parcela Contrato', 'Total Mensal'])
            for mes in range(1, 13): # 12 parcelas do orçamento 
                p_contrato = valor_mensal_contrato if mes <= self.parcelas_contrato else 0
                total = self.mensalidade_base + p_contrato
                writer.writerow([mes, f"{self.mensalidade_base:.2f}", f"{p_contrato:.2f}", f"{total:.2f}"])
        return filename

# Exemplo de uso para demonstração no vídeo
if __name__ == "__main__":
    # Teste: Apartamento, 2 quartos, com garagem, sem crianças, contrato em 5x
    app = OrcamentoImobiliaria("Cliente_Exemplo", "apartamento", 2, True, False, 5)
    app.calcular_aluguel()
    arquivo = app.gerar_csv()
    print(f"Orçamento gerado com sucesso: {arquivo}")