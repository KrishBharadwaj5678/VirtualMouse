<p align="center">
  <img src="https://komarev.com/ghpvc/?username=KrishBharadwaj5678&label=Profile%20Views&color=brightgreen&style=for-the-badge" />
  <img src="https://hits.sh/github.com/KrishBharadwaj5678/VirtualMouse.svg?style=for-the-badge&label=Repo%20Views&color=blue" />
  <img src="https://img.shields.io/github/stars/KrishBharadwaj5678/VirtualMouse?style=for-the-badge&color=yellow" />
  <img src="https://img.shields.io/github/last-commit/KrishBharadwaj5678/VirtualMouse?style=for-the-badge&color=orange" />
  <img src="https://img.shields.io/github/repo-size/KrishBharadwaj5678/VirtualMouse?style=for-the-badge&color=blue" />
</p>

<p align="center">
  <a href="README.md">English</a> |
  <a href="README.pt.md">Português</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.ru.md">Русский</a>
</p>

<h1 align="center"><img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/icons/virtualMouse.png" width="35"/> Mouse Virtual</h1>

<p align="center">
   O Mouse Virtual permite controlar o computador usando gestos das mãos detectados pela webcam, proporcionando uma forma de interação com a tela sem a necessidade de contato físico.
</p>

<p align="center">
  <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/demos/virtualMouse.gif" width="100%" />
</p>

<img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/divider.gif" width="100%"/>

## <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/features.gif" width="35"/> Recursos

| Recurso                       | Descrição                                                                          |
| ----------------------------- | ---------------------------------------------------------------------------------- |
| 🖐️ Controle por Gestos       | Use sua mão para mover o ponteiro do mouse em tempo real.                         |
| 👆 Ações de Clique            | **Clique esquerdo**, **direito** e **duplo clique** usando gestos dos dedos.      |
| ↕️ Rolar para Cima / Baixo   | Role pelas páginas usando movimentos dos dedos.                                   |
| 🖱️ Movimento do Cursor       | Mova suavemente o cursor do mouse com base na posição da mão.                     |
| ⚡ Rastreamento em Tempo Real | Rastreamento rápido e responsivo usando **OpenCV** e **MediaPipe**.               |
| 🤟 Reconhecimento de Gestos  | Detecte configurações específicas dos dedos para diferentes comandos.             |

<img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/divider.gif" width="100%"/>

## <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/techStack.gif" width="35"/> Tecnologias Utilizadas

| Tecnologia | Finalidade |
| ---------- | ---------- |
| <img src="https://skillicons.dev/icons?i=python" width="25"/> **Python3** | Linguagem de programação principal |
| <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/icons/opencv.png" width="25"/> **OpenCV** | Captura de vídeo e processamento de imagens |
| <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/icons/mediapipe.png" width="25"/> **MediaPipe** | Rastreamento das mãos e detecção de gestos |
| <img src="https://skillicons.dev/icons?i=python" width="25"/> **PyAutoGUI** | Simulação de ações do mouse |
| <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/icons/numpy.png" width="25"/> **NumPy** | Operações numéricas eficientes |

<img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/divider.gif" width="100%"/>

## <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/gettingStarted.gif" width="35"/> Primeiros Passos

### 1️⃣ Clone o Repositório

```bash
git clone https://github.com/KrishBharadwaj5678/VirtualMouse.git
````

### 2️⃣ Navegue até o Projeto

```
cd VirtualMouse
```

### 3️⃣ Instale as Dependências

```
pip install -r requirements.txt
```

### 4️⃣ Execute o Aplicativo

```
python app.py
```

 <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/divider.gif" width="100%"/> 
 
 ## <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/howItWorks.gif" width="35"/> Instruções de Gestos

 <p align="center"> 
   <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/demos/fingerNames.png"/>
 </p> 
 
| Ação | Posição dos Dedos | Limite de Distância |
| --- | --- | --- |
| **Clique Esquerdo** | Indicador 🔼, Médio 🔼 | Indicador ↔️ Médio < 25px |
| **Clique Direito** | Indicador 🔼, Médio 🔼, Mínimo 🔼 | Indicador ↔️ Médio < 25px |
| **Rolar para Baixo** | Indicador 🔼, Médio 🔼, Polegar 🔼 | Indicador ↔️ Médio < 25px |
| **Rolar para Cima** | Indicador 🔼, Médio 🔼, Mínimo 🔼, Polegar 🔼 | Indicador ↔️ Médio < 25px |
| **Duplo Clique** | Indicador 🔼, Polegar 🔼 | Não Necessário |

- 🔼 = Dedo levantado
- ↔️ = Distância entre as pontas dos dedos

<img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/divider.gif" width="100%"/> 

## <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/license.gif" width="35"/> Licença

Este projeto está licenciado sob a **Licença MIT**.

Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.

<p align="center"> 
  <img src="https://github.com/KrishBharadwaj5678/VirtualMouse/raw/main/assets/readme/footer.gif" width="320px"/> 
</p>
