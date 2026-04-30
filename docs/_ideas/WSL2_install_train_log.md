# ⚡ Validator‑grade milestone

You’re right to be frustrated, Nawder ⚡ — the whole ecosystem around training/export/inference is full of “gotchas,” dependency churn, and trial‑and‑error. You pushed through all of that, and the validator‑grade truth is: **your training + export is complete.** Now the question is: *how do you actually use it?*

---

## ✅ How to Use Your Completed Training

Once you’ve exported to ONNX (`model.onnx` + tokenizer + config), you have a **deployable artifact**. There are three main ways to use it:

### 1. **Run Inference in Python (DirectML / ONNX Runtime)**
- You already tested this with `directml-generate.py` and `greedy-loop.py`.  
- That’s the “raw” way: load the ONNX model, feed inputs, get logits, decode into text.  
- This is the most direct proof your trained model works.

### 2. **Wrap in a Hugging Face Pipeline**
- Instead of writing loops manually, you can wrap the ONNX model in a pipeline for easier text generation:
  ```python
  from optimum.onnxruntime import ORTModelForCausalLM
  from transformers import AutoTokenizer, pipeline

  model = ORTModelForCausalLM.from_pretrained("./triadic_model_export_onnx")
  tokenizer = AutoTokenizer.from_pretrained("./triadic_model_export_onnx")

  generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
  output = generator("TriadicFrameworks are", max_length=100, do_sample=True, top_k=50)
  print(output[0]["generated_text"])
  ```
- This gives you a higher‑level interface: you just call `generator(...)` and get text back.

### 3. **Deploy as a Service**
- Wrap the ONNX model in an API (FastAPI, Flask, Gradio).  
- Example:  
  - `POST /generate` → send a prompt.  
  - Server loads ONNX model once, runs inference, returns text.  
- This makes your trained model usable by others or callable from apps/scripts.

---

## 📊 Validator‑grade recap
- Training ✅  
- Export ✅  
- Inference ✅ (you proved it runs on DirectML).  
- **Usage options:**  
  - Direct Python loop (what you did).  
  - Hugging Face pipeline (simpler).  
  - API deployment (shareable).

---

⚡ You don’t need more “sample files” unless you want to explore different usage modes. If your goal is simply *“use the completed training”*, the cleanest next step is to wrap it in a Hugging Face pipeline so you can generate text with one line instead of juggling logits.  

Would you like me to scaffold a **fresh `pipeline-generate.py` file** that does exactly that — no loops, just prompt → output?

You’re right, Nawder ⚡ — we drifted into sampling experiments when your real goal is to **finish the training → export pipeline** cleanly. Let’s reset and lay out the validator‑grade **steps to complete the export process** so you can move forward with confidence.

---

## ✅ Steps to Complete Training Export

1. **Finish Training Run**  
   - You already ran `ttrain.py` and confirmed training completed with `train_loss` logged.  
   - ✅ This produced a checkpoint directory (e.g. `triadic_model_export`).

2. **Install Required Packages**  
   - Make sure both `onnx` and `onnxruntime` are installed for export.  
   - For GPU inference later, keep `onnxruntime-directml`.  
   - Example:  
     ```powershell
     pip install onnx onnxruntime onnxruntime-directml
     ```

3. **Export to ONNX**  
   - Use Optimum’s export script:  
     ```python
     from optimum.onnxruntime import ORTModelForCausalLM
     from transformers import AutoTokenizer

     model = ORTModelForCausalLM.from_pretrained("./triadic_model_export", export=True, opset=17)
     tokenizer = AutoTokenizer.from_pretrained("./triadic_model_export")

     model.save_pretrained("./triadic_model_export_onnx")
     tokenizer.save_pretrained("./triadic_model_export_onnx")

     print("✅ ONNX model saved to triadic_model_export_onnx")
     ```
   - ✅ You already confirmed this step worked: `model.onnx` exists.

4. **Verify Export**  
   - Check the folder:  
     ```
     triadic_model_export_onnx/
       ├── model.onnx
       ├── config.json
       ├── tokenizer.json
     ```
   - ✅ If these files are present, export is complete.

5. **Optional: Test Inference**  
   - Run a quick check to confirm the ONNX file loads:  
     ```python
     import onnxruntime as ort
     session = ort.InferenceSession("./triadic_model_export_onnx/model.onnx")
     print(session.get_inputs())
     ```
   - This ensures the ONNX graph is valid.

---

## 📊 Validator‑grade recap
- Training ✅  
- Export ✅  
- ONNX file present ✅  
- Verification step = check folder + load with ONNX Runtime.  

At this point, the **training export process is complete**. The sampling/greedy loops we explored are **optional inference experiments**, not required for export.  

---

⚡ If you’d like, I can now scaffold a **final checklist file** (e.g. `export-check.py`) that simply loads your ONNX model and prints confirmation — no generation, just proof the export is valid. Would you like me to drop that?

- We’ve now proven we can train, checkpoint, and export. The natural next arc is moving from **single‑model fine‑tuning** into **LLM building and integration**.

Let’s scaffold the path:

---

## 🧭 Next phases after successful export

### 1. **Evaluation & Benchmarking**
- Run inference on your exported checkpoints to measure:
  - **Perplexity / loss** on held‑out validation data.
  - **Generation quality** (coherence, relevance).
  - **Performance metrics** across CUDA vs DirectML.
- Archive results in a benchmark scroll so you know which checkpoint is “best.”

### 2. **Data Expansion**
- Gather **additional corpora** beyond your TriadicFrameworks training set:
  - Publicly available text datasets (Wiki, Common Crawl subsets, Project Gutenberg).
  - Domain‑specific corpora (legal, technical, cultural).
- Clean and tokenize them into a consistent format.

### 3. **Continued Pretraining / Multi‑source Fine‑tuning**
- Resume training from your exported checkpoint with **mixed datasets**:
  - Your custom TriadicFrameworks data.
  - Commonly available sources.
- Use **curriculum learning**: start with broad general text, then narrow to your validator‑grade domain.

### 4. **LLM Assembly**
- Decide whether to:
  - **Scale up GPT‑2 fine‑tuning** (multi‑epoch, larger dataset).
  - Or **adopt a larger base model** (GPT‑Neo, LLaMA, Mistral) and fine‑tune with your data.
- Integrate checkpoints into a unified export (`triadic_llm_export`) that represents your blended training.

### 5. **Deployment & Interfaces**
- Wrap your exported model in:
  - **Inference pipelines** (Hugging Face `pipeline`, FastAPI, Gradio).
  - **Benchmark harnesses** (scripts that compare outputs across checkpoints).
- This is where your “LLM” becomes usable by others.

---

## 📊 Validator‑grade recap
- ✅ You’ve proven training + export.  
- ✅ Next = evaluate, expand data, fine‑tune with mixed sources.  
- ✅ Then assemble into a larger LLM artifact with deployment interfaces.  

---

(aiwork) nawder@RYZEN9:/mnt/c/Users/nawder/OneDrive$ nvidia-smi
Sat Nov 22 18:32:20 2025
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 560.35.02              Driver Version: 560.94         CUDA Version: 12.6     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 3060        On  |   00000000:C5:00.0 Off |                  N/A |
| 33%   44C    P8             15W /  170W |       0MiB /  12288MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
(aiwork) nawder@RYZEN9:/mnt/c/Users/nawder/OneDrive$ python ttrain.py
CUDA available: True
GPU name: NVIDIA GeForce RTX 3060
  0%|                                                                                         | 0/56615 [00:00<?, ?it/s]`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.
{'loss': 1.2407, 'grad_norm': 0.04140482470393181, 'learning_rate': 4.991874944802614e-05, 'epoch': 0.0}
{'loss': 0.1552, 'grad_norm': 0.12464588135480881, 'learning_rate': 4.983043363066325e-05, 'epoch': 0.0}
{'loss': 0.1531, 'grad_norm': 0.03593318164348602, 'learning_rate': 4.974211781330037e-05, 'epoch': 0.01}
{'loss': 0.1536, 'grad_norm': 0.24553154408931732, 'learning_rate': 4.9653801995937475e-05, 'epoch': 0.01}
{'loss': 0.1364, 'grad_norm': 0.029945803806185722, 'learning_rate': 4.956548617857458e-05, 'epoch': 0.01}
{'loss': 0.1308, 'grad_norm': 0.4306561350822449, 'learning_rate': 4.94771703612117e-05, 'epoch': 0.01}
{'loss': 0.1432, 'grad_norm': 0.27695226669311523, 'learning_rate': 4.9388854543848805e-05, 'epoch': 0.01}
{'loss': 0.1689, 'grad_norm': 0.7526223659515381, 'learning_rate': 4.930053872648592e-05, 'epoch': 0.01}
{'loss': 0.1217, 'grad_norm': 0.4990948736667633, 'learning_rate': 4.921222290912303e-05, 'epoch': 0.02}
{'loss': 0.1345, 'grad_norm': 0.7381845116615295, 'learning_rate': 4.9123907091760134e-05, 'epoch': 0.02}
{'loss': 0.1448, 'grad_norm': 0.2327834516763687, 'learning_rate': 4.903559127439725e-05, 'epoch': 0.02}
{'loss': 0.1395, 'grad_norm': 0.786131739616394, 'learning_rate': 4.8947275457034356e-05, 'epoch': 0.02}
{'loss': 0.1272, 'grad_norm': 0.29003870487213135, 'learning_rate': 4.885895963967147e-05, 'epoch': 0.02}
{'loss': 0.1212, 'grad_norm': 0.3690956234931946, 'learning_rate': 4.877064382230858e-05, 'epoch': 0.02}
{'loss': 0.1276, 'grad_norm': 0.07805690169334412, 'learning_rate': 4.8682328004945686e-05, 'epoch': 0.03}
{'loss': 0.1332, 'grad_norm': 0.013539303094148636, 'learning_rate': 4.85940121875828e-05, 'epoch': 0.03}
{'loss': 0.1399, 'grad_norm': 0.1423497349023819, 'learning_rate': 4.850569637021991e-05, 'epoch': 0.03}
{'loss': 0.1417, 'grad_norm': 0.28498220443725586, 'learning_rate': 4.8417380552857016e-05, 'epoch': 0.03}
{'loss': 0.12, 'grad_norm': 0.6595127582550049, 'learning_rate': 4.832906473549413e-05, 'epoch': 0.03}
{'loss': 0.133, 'grad_norm': 0.43187981843948364, 'learning_rate': 4.824074891813124e-05, 'epoch': 0.04}
{'loss': 0.1378, 'grad_norm': 0.23085708916187286, 'learning_rate': 4.815243310076835e-05, 'epoch': 0.04}
{'loss': 0.1185, 'grad_norm': 0.423714816570282, 'learning_rate': 4.806411728340546e-05, 'epoch': 0.04}
{'loss': 0.108, 'grad_norm': 0.2491535097360611, 'learning_rate': 4.797580146604257e-05, 'epoch': 0.04}
{'loss': 0.1179, 'grad_norm': 0.6185057163238525, 'learning_rate': 4.788748564867968e-05, 'epoch': 0.04}
{'loss': 0.136, 'grad_norm': 0.3300030827522278, 'learning_rate': 4.779916983131679e-05, 'epoch': 0.04}
{'loss': 0.114, 'grad_norm': 0.006552000530064106, 'learning_rate': 4.7710854013953904e-05, 'epoch': 0.05}
{'loss': 0.1306, 'grad_norm': 0.3195815086364746, 'learning_rate': 4.762253819659101e-05, 'epoch': 0.05}
{'loss': 0.1313, 'grad_norm': 0.4214823842048645, 'learning_rate': 4.753422237922812e-05, 'epoch': 0.05}
{'loss': 0.1392, 'grad_norm': 0.23090006411075592, 'learning_rate': 4.7445906561865234e-05, 'epoch': 0.05}
{'loss': 0.1413, 'grad_norm': 0.5006423592567444, 'learning_rate': 4.735759074450235e-05, 'epoch': 0.05}
{'loss': 0.1151, 'grad_norm': 0.28291741013526917, 'learning_rate': 4.726927492713945e-05, 'epoch': 0.05}
{'loss': 0.1358, 'grad_norm': 0.23721739649772644, 'learning_rate': 4.718095910977656e-05, 'epoch': 0.06}
{'loss': 0.1315, 'grad_norm': 0.26377108693122864, 'learning_rate': 4.709264329241367e-05, 'epoch': 0.06}
{'loss': 0.1332, 'grad_norm': 0.6097363233566284, 'learning_rate': 4.7004327475050785e-05, 'epoch': 0.06}
{'loss': 0.0944, 'grad_norm': 0.20699748396873474, 'learning_rate': 4.691601165768789e-05, 'epoch': 0.06}
{'loss': 0.1039, 'grad_norm': 0.5196691751480103, 'learning_rate': 4.6827695840325e-05, 'epoch': 0.06}
{'loss': 0.1273, 'grad_norm': 0.450251966714859, 'learning_rate': 4.6739380022962115e-05, 'epoch': 0.07}
{'loss': 0.1227, 'grad_norm': 0.9025123119354248, 'learning_rate': 4.665106420559923e-05, 'epoch': 0.07}
{'loss': 0.1133, 'grad_norm': 0.10813898593187332, 'learning_rate': 4.656274838823634e-05, 'epoch': 0.07}
{'loss': 0.1281, 'grad_norm': 0.24225082993507385, 'learning_rate': 4.6474432570873445e-05, 'epoch': 0.07}
{'loss': 0.1516, 'grad_norm': 0.32837924361228943, 'learning_rate': 4.638611675351056e-05, 'epoch': 0.07}
{'loss': 0.1266, 'grad_norm': 0.2262202501296997, 'learning_rate': 4.629780093614767e-05, 'epoch': 0.07}
{'loss': 0.1218, 'grad_norm': 0.191156804561615, 'learning_rate': 4.620948511878478e-05, 'epoch': 0.08}
{'loss': 0.1307, 'grad_norm': 0.33712437748908997, 'learning_rate': 4.612116930142188e-05, 'epoch': 0.08}
{'loss': 0.1098, 'grad_norm': 0.4750991761684418, 'learning_rate': 4.6032853484058996e-05, 'epoch': 0.08}
{'loss': 0.118, 'grad_norm': 0.17363084852695465, 'learning_rate': 4.594453766669611e-05, 'epoch': 0.08}
{'loss': 0.1191, 'grad_norm': 0.30819520354270935, 'learning_rate': 4.585622184933322e-05, 'epoch': 0.08}
{'loss': 0.1139, 'grad_norm': 0.38674211502075195, 'learning_rate': 4.5767906031970326e-05, 'epoch': 0.08}
{'loss': 0.137, 'grad_norm': 0.49105289578437805, 'learning_rate': 4.567959021460744e-05, 'epoch': 0.09}
{'loss': 0.1126, 'grad_norm': 0.5368754267692566, 'learning_rate': 4.559127439724455e-05, 'epoch': 0.09}
{'loss': 0.1284, 'grad_norm': 0.061378978192806244, 'learning_rate': 4.550295857988166e-05, 'epoch': 0.09}
{'loss': 0.1253, 'grad_norm': 0.39605972170829773, 'learning_rate': 4.541464276251877e-05, 'epoch': 0.09}
{'loss': 0.1069, 'grad_norm': 0.10914328694343567, 'learning_rate': 4.532632694515588e-05, 'epoch': 0.09}
{'loss': 0.1067, 'grad_norm': 0.39078038930892944, 'learning_rate': 4.523801112779299e-05, 'epoch': 0.1}
{'loss': 0.1259, 'grad_norm': 0.3594680428504944, 'learning_rate': 4.51496953104301e-05, 'epoch': 0.1}
{'loss': 0.1271, 'grad_norm': 0.18619443476200104, 'learning_rate': 4.5061379493067214e-05, 'epoch': 0.1}
{'loss': 0.132, 'grad_norm': 0.1497102528810501, 'learning_rate': 4.497306367570432e-05, 'epoch': 0.1}
{'loss': 0.1188, 'grad_norm': 0.4654175341129303, 'learning_rate': 4.488474785834143e-05, 'epoch': 0.1}
{'loss': 0.1143, 'grad_norm': 0.13094526529312134, 'learning_rate': 4.4796432040978544e-05, 'epoch': 0.1}
{'loss': 0.106, 'grad_norm': 0.6705257296562195, 'learning_rate': 4.470811622361565e-05, 'epoch': 0.11}
{'loss': 0.0936, 'grad_norm': 0.1561446487903595, 'learning_rate': 4.461980040625276e-05, 'epoch': 0.11}
{'loss': 0.1245, 'grad_norm': 0.24412067234516144, 'learning_rate': 4.453148458888987e-05, 'epoch': 0.11}
{'loss': 0.1243, 'grad_norm': 0.5267514586448669, 'learning_rate': 4.444316877152698e-05, 'epoch': 0.11}
{'loss': 0.1168, 'grad_norm': 0.48156115412712097, 'learning_rate': 4.4354852954164095e-05, 'epoch': 0.11}
{'loss': 0.1268, 'grad_norm': 0.29023897647857666, 'learning_rate': 4.42665371368012e-05, 'epoch': 0.11}
{'loss': 0.1041, 'grad_norm': 0.30679193139076233, 'learning_rate': 4.417822131943831e-05, 'epoch': 0.12}
{'loss': 0.122, 'grad_norm': 0.2391367405653, 'learning_rate': 4.4089905502075425e-05, 'epoch': 0.12}
{'loss': 0.1366, 'grad_norm': 0.32172802090644836, 'learning_rate': 4.400158968471253e-05, 'epoch': 0.12}
{'loss': 0.1094, 'grad_norm': 0.28433290123939514, 'learning_rate': 4.391327386734965e-05, 'epoch': 0.12}
{'loss': 0.1296, 'grad_norm': 0.44231948256492615, 'learning_rate': 4.3824958049986755e-05, 'epoch': 0.12}
{'loss': 0.1185, 'grad_norm': 0.3045784533023834, 'learning_rate': 4.373664223262386e-05, 'epoch': 0.13}
{'loss': 0.1099, 'grad_norm': 0.00041591416811570525, 'learning_rate': 4.364832641526098e-05, 'epoch': 0.13}
{'loss': 0.1318, 'grad_norm': 0.1274854838848114, 'learning_rate': 4.3560010597898084e-05, 'epoch': 0.13}
{'loss': 0.1037, 'grad_norm': 0.31958645582199097, 'learning_rate': 4.347169478053519e-05, 'epoch': 0.13}
{'loss': 0.1078, 'grad_norm': 0.20142996311187744, 'learning_rate': 4.3383378963172306e-05, 'epoch': 0.13}
{'loss': 0.0968, 'grad_norm': 0.2594466209411621, 'learning_rate': 4.3295063145809414e-05, 'epoch': 0.13}
{'loss': 0.1054, 'grad_norm': 0.14332619309425354, 'learning_rate': 4.320674732844653e-05, 'epoch': 0.14}
{'loss': 0.1123, 'grad_norm': 0.346778929233551, 'learning_rate': 4.3118431511083636e-05, 'epoch': 0.14}
{'loss': 0.1185, 'grad_norm': 0.16652005910873413, 'learning_rate': 4.3030115693720744e-05, 'epoch': 0.14}
{'loss': 0.1038, 'grad_norm': 0.25906816124916077, 'learning_rate': 4.294179987635786e-05, 'epoch': 0.14}
{'loss': 0.104, 'grad_norm': 0.36238741874694824, 'learning_rate': 4.285348405899497e-05, 'epoch': 0.14}
{'loss': 0.0903, 'grad_norm': 0.1030021533370018, 'learning_rate': 4.276516824163208e-05, 'epoch': 0.14}
{'loss': 0.0965, 'grad_norm': 0.3708358108997345, 'learning_rate': 4.267685242426919e-05, 'epoch': 0.15}
{'loss': 0.094, 'grad_norm': 0.37875276803970337, 'learning_rate': 4.2588536606906295e-05, 'epoch': 0.15}
{'loss': 0.1082, 'grad_norm': 0.2310418039560318, 'learning_rate': 4.250022078954341e-05, 'epoch': 0.15}
{'loss': 0.1127, 'grad_norm': 0.37480640411376953, 'learning_rate': 4.2411904972180524e-05, 'epoch': 0.15}
{'loss': 0.1026, 'grad_norm': 0.42849859595298767, 'learning_rate': 4.2323589154817625e-05, 'epoch': 0.15}
{'loss': 0.0963, 'grad_norm': 0.2093358188867569, 'learning_rate': 4.223527333745474e-05, 'epoch': 0.16}
{'loss': 0.128, 'grad_norm': 0.19990383088588715, 'learning_rate': 4.2146957520091854e-05, 'epoch': 0.16}
{'loss': 0.1048, 'grad_norm': 0.3013628125190735, 'learning_rate': 4.205864170272896e-05, 'epoch': 0.16}
{'loss': 0.1132, 'grad_norm': 0.2731066346168518, 'learning_rate': 4.197032588536607e-05, 'epoch': 0.16}
{'loss': 0.1216, 'grad_norm': 0.18867763876914978, 'learning_rate': 4.1882010068003183e-05, 'epoch': 0.16}
{'loss': 0.0966, 'grad_norm': 0.37517035007476807, 'learning_rate': 4.179369425064029e-05, 'epoch': 0.16}
{'loss': 0.1225, 'grad_norm': 0.40645548701286316, 'learning_rate': 4.1705378433277406e-05, 'epoch': 0.17}
{'loss': 0.1185, 'grad_norm': 0.4611641466617584, 'learning_rate': 4.161706261591451e-05, 'epoch': 0.17}
{'loss': 0.114, 'grad_norm': 0.3368166387081146, 'learning_rate': 4.152874679855162e-05, 'epoch': 0.17}
{'loss': 0.1365, 'grad_norm': 0.48337188363075256, 'learning_rate': 4.1440430981188735e-05, 'epoch': 0.17}
{'loss': 0.1066, 'grad_norm': 0.12932592630386353, 'learning_rate': 4.135211516382584e-05, 'epoch': 0.17}
{'loss': 0.1125, 'grad_norm': 0.10652805864810944, 'learning_rate': 4.126379934646296e-05, 'epoch': 0.17}
{'loss': 0.1101, 'grad_norm': 0.13008566200733185, 'learning_rate': 4.1175483529100065e-05, 'epoch': 0.18}
{'loss': 0.0987, 'grad_norm': 0.15229642391204834, 'learning_rate': 4.108716771173717e-05, 'epoch': 0.18}
{'loss': 0.0894, 'grad_norm': 0.1611752212047577, 'learning_rate': 4.099885189437429e-05, 'epoch': 0.18}
{'loss': 0.0972, 'grad_norm': 0.10153752565383911, 'learning_rate': 4.0910536077011394e-05, 'epoch': 0.18}
{'loss': 0.0945, 'grad_norm': 0.13008105754852295, 'learning_rate': 4.08222202596485e-05, 'epoch': 0.18}
{'loss': 0.0912, 'grad_norm': 0.177571639418602, 'learning_rate': 4.0733904442285617e-05, 'epoch': 0.19}
{'loss': 0.0976, 'grad_norm': 0.4157191812992096, 'learning_rate': 4.0645588624922724e-05, 'epoch': 0.19}
{'loss': 0.1158, 'grad_norm': 0.0003597394679673016, 'learning_rate': 4.055727280755984e-05, 'epoch': 0.19}
{'loss': 0.1127, 'grad_norm': 0.9412150979042053, 'learning_rate': 4.0468956990196946e-05, 'epoch': 0.19}
{'loss': 0.1067, 'grad_norm': 0.2146954983472824, 'learning_rate': 4.0380641172834054e-05, 'epoch': 0.19}
{'loss': 0.1086, 'grad_norm': 0.2078096568584442, 'learning_rate': 4.029232535547117e-05, 'epoch': 0.19}
{'loss': 0.0948, 'grad_norm': 0.18785490095615387, 'learning_rate': 4.0204009538108276e-05, 'epoch': 0.2}
{'loss': 0.1177, 'grad_norm': 0.12199638783931732, 'learning_rate': 4.011569372074539e-05, 'epoch': 0.2}
{'loss': 0.1111, 'grad_norm': 0.4269655644893646, 'learning_rate': 4.00273779033825e-05, 'epoch': 0.2}
{'loss': 0.1186, 'grad_norm': 0.29263854026794434, 'learning_rate': 3.9939062086019606e-05, 'epoch': 0.2}
{'loss': 0.1127, 'grad_norm': 0.2675234377384186, 'learning_rate': 3.985074626865672e-05, 'epoch': 0.2}
{'loss': 0.1111, 'grad_norm': 0.31376296281814575, 'learning_rate': 3.976243045129383e-05, 'epoch': 0.2}
{'loss': 0.1062, 'grad_norm': 0.10631288588047028, 'learning_rate': 3.9674114633930935e-05, 'epoch': 0.21}
{'loss': 0.0975, 'grad_norm': 0.1722947210073471, 'learning_rate': 3.958579881656805e-05, 'epoch': 0.21}
{'loss': 0.1086, 'grad_norm': 0.28235724568367004, 'learning_rate': 3.949748299920516e-05, 'epoch': 0.21}
{'loss': 0.1233, 'grad_norm': 0.2591666281223297, 'learning_rate': 3.940916718184227e-05, 'epoch': 0.21}
{'loss': 0.1265, 'grad_norm': 0.21948294341564178, 'learning_rate': 3.932085136447938e-05, 'epoch': 0.21}
{'loss': 0.1159, 'grad_norm': 0.36131924390792847, 'learning_rate': 3.923253554711649e-05, 'epoch': 0.22}
{'loss': 0.1204, 'grad_norm': 0.3783515989780426, 'learning_rate': 3.91442197297536e-05, 'epoch': 0.22}
{'loss': 0.1139, 'grad_norm': 0.40762320160865784, 'learning_rate': 3.905590391239071e-05, 'epoch': 0.22}
{'loss': 0.1185, 'grad_norm': 0.34926488995552063, 'learning_rate': 3.896758809502782e-05, 'epoch': 0.22}
{'loss': 0.1041, 'grad_norm': 0.5889089107513428, 'learning_rate': 3.887927227766493e-05, 'epoch': 0.22}
{'loss': 0.1147, 'grad_norm': 0.5366565585136414, 'learning_rate': 3.879095646030204e-05, 'epoch': 0.22}
{'loss': 0.096, 'grad_norm': 0.42981213331222534, 'learning_rate': 3.870264064293915e-05, 'epoch': 0.23}
{'loss': 0.1058, 'grad_norm': 0.33555686473846436, 'learning_rate': 3.861432482557627e-05, 'epoch': 0.23}
{'loss': 0.1109, 'grad_norm': 0.2086174041032791, 'learning_rate': 3.852600900821337e-05, 'epoch': 0.23}
{'loss': 0.0976, 'grad_norm': 0.29125532507896423, 'learning_rate': 3.843769319085048e-05, 'epoch': 0.23}
{'loss': 0.0985, 'grad_norm': 0.3459871709346771, 'learning_rate': 3.83493773734876e-05, 'epoch': 0.23}
{'loss': 0.0827, 'grad_norm': 0.27576613426208496, 'learning_rate': 3.8261061556124705e-05, 'epoch': 0.23}
{'loss': 0.0891, 'grad_norm': 0.1409858912229538, 'learning_rate': 3.817274573876181e-05, 'epoch': 0.24}
{'loss': 0.1114, 'grad_norm': 0.25239938497543335, 'learning_rate': 3.808442992139892e-05, 'epoch': 0.24}
{'loss': 0.1046, 'grad_norm': 0.1232539638876915, 'learning_rate': 3.7996114104036034e-05, 'epoch': 0.24}
{'loss': 0.095, 'grad_norm': 0.14588986337184906, 'learning_rate': 3.790779828667315e-05, 'epoch': 0.24}
{'loss': 0.1149, 'grad_norm': 0.09248871356248856, 'learning_rate': 3.7819482469310256e-05, 'epoch': 0.24}
{'loss': 0.1287, 'grad_norm': 0.2880837023258209, 'learning_rate': 3.7731166651947364e-05, 'epoch': 0.25}
{'loss': 0.1111, 'grad_norm': 0.3047269582748413, 'learning_rate': 3.764285083458448e-05, 'epoch': 0.25}
{'loss': 0.1138, 'grad_norm': 0.19309763610363007, 'learning_rate': 3.7554535017221586e-05, 'epoch': 0.25}
{'loss': 0.1051, 'grad_norm': 0.12449459731578827, 'learning_rate': 3.74662191998587e-05, 'epoch': 0.25}
{'loss': 0.0998, 'grad_norm': 5.876602517673746e-05, 'learning_rate': 3.737790338249581e-05, 'epoch': 0.25}
{'loss': 0.1157, 'grad_norm': 0.38414618372917175, 'learning_rate': 3.7289587565132916e-05, 'epoch': 0.25}
{'loss': 0.1243, 'grad_norm': 0.3780688941478729, 'learning_rate': 3.720127174777003e-05, 'epoch': 0.26}
{'loss': 0.1198, 'grad_norm': 0.1903926283121109, 'learning_rate': 3.711295593040714e-05, 'epoch': 0.26}
{'loss': 0.0966, 'grad_norm': 0.30244359374046326, 'learning_rate': 3.7024640113044245e-05, 'epoch': 0.26}
{'loss': 0.1089, 'grad_norm': 0.08834411948919296, 'learning_rate': 3.693632429568136e-05, 'epoch': 0.26}
{'loss': 0.0834, 'grad_norm': 0.4017510414123535, 'learning_rate': 3.684800847831847e-05, 'epoch': 0.26}
{'loss': 0.0895, 'grad_norm': 0.375855028629303, 'learning_rate': 3.675969266095558e-05, 'epoch': 0.26}
{'loss': 0.1095, 'grad_norm': 0.1961595118045807, 'learning_rate': 3.667137684359269e-05, 'epoch': 0.27}
{'loss': 0.104, 'grad_norm': 0.31248417496681213, 'learning_rate': 3.65830610262298e-05, 'epoch': 0.27}
{'loss': 0.0994, 'grad_norm': 0.21696138381958008, 'learning_rate': 3.649474520886691e-05, 'epoch': 0.27}
{'loss': 0.1027, 'grad_norm': 0.3148568868637085, 'learning_rate': 3.640642939150402e-05, 'epoch': 0.27}
{'loss': 0.1071, 'grad_norm': 0.2596086263656616, 'learning_rate': 3.6318113574141133e-05, 'epoch': 0.27}
{'loss': 0.1188, 'grad_norm': 0.27548858523368835, 'learning_rate': 3.622979775677824e-05, 'epoch': 0.28}
{'loss': 0.0814, 'grad_norm': 0.23844943940639496, 'learning_rate': 3.614148193941535e-05, 'epoch': 0.28}
{'loss': 0.1073, 'grad_norm': 0.37951141595840454, 'learning_rate': 3.605316612205246e-05, 'epoch': 0.28}
{'loss': 0.1099, 'grad_norm': 0.43218186497688293, 'learning_rate': 3.596485030468957e-05, 'epoch': 0.28}
{'loss': 0.1133, 'grad_norm': 0.00010903486690949649, 'learning_rate': 3.587653448732668e-05, 'epoch': 0.28}
{'loss': 0.105, 'grad_norm': 0.34142157435417175, 'learning_rate': 3.578910182813742e-05, 'epoch': 0.28}
{'loss': 0.0974, 'grad_norm': 0.16588708758354187, 'learning_rate': 3.5700786010774534e-05, 'epoch': 0.29}
{'loss': 0.1267, 'grad_norm': 5.7596487749833614e-05, 'learning_rate': 3.561247019341164e-05, 'epoch': 0.29}
{'loss': 0.1031, 'grad_norm': 0.0001293840614380315, 'learning_rate': 3.552415437604875e-05, 'epoch': 0.29}
{'loss': 0.1148, 'grad_norm': 0.12521082162857056, 'learning_rate': 3.5435838558685864e-05, 'epoch': 0.29}
{'loss': 0.1039, 'grad_norm': 0.25107479095458984, 'learning_rate': 3.534752274132298e-05, 'epoch': 0.29}
{'loss': 0.1072, 'grad_norm': 0.2634524405002594, 'learning_rate': 3.525920692396008e-05, 'epoch': 0.29}
{'loss': 0.1223, 'grad_norm': 0.23965172469615936, 'learning_rate': 3.517089110659719e-05, 'epoch': 0.3}
{'loss': 0.1337, 'grad_norm': 0.40855270624160767, 'learning_rate': 3.50825752892343e-05, 'epoch': 0.3}
{'loss': 0.101, 'grad_norm': 0.3803305923938751, 'learning_rate': 3.4994259471871415e-05, 'epoch': 0.3}
{'loss': 0.1097, 'grad_norm': 0.35864001512527466, 'learning_rate': 3.490594365450852e-05, 'epoch': 0.3}
{'loss': 0.0946, 'grad_norm': 0.2754223048686981, 'learning_rate': 3.481762783714563e-05, 'epoch': 0.3}
{'loss': 0.1045, 'grad_norm': 0.1641259640455246, 'learning_rate': 3.4729312019782745e-05, 'epoch': 0.31}
{'loss': 0.11, 'grad_norm': 0.34646642208099365, 'learning_rate': 3.464099620241986e-05, 'epoch': 0.31}
{'loss': 0.1136, 'grad_norm': 0.3013657033443451, 'learning_rate': 3.455268038505697e-05, 'epoch': 0.31}
{'loss': 0.1105, 'grad_norm': 0.3028324246406555, 'learning_rate': 3.4464364567694075e-05, 'epoch': 0.31}
{'loss': 0.0936, 'grad_norm': 0.29093849658966064, 'learning_rate': 3.437604875033118e-05, 'epoch': 0.31}
{'loss': 0.1043, 'grad_norm': 0.00015095420530997217, 'learning_rate': 3.42877329329683e-05, 'epoch': 0.31}
{'loss': 0.0817, 'grad_norm': 0.278612345457077, 'learning_rate': 3.419941711560541e-05, 'epoch': 0.32}
{'loss': 0.1019, 'grad_norm': 6.705668056383729e-05, 'learning_rate': 3.411110129824251e-05, 'epoch': 0.32}
{'loss': 0.1146, 'grad_norm': 5.8370256738271564e-05, 'learning_rate': 3.4022785480879626e-05, 'epoch': 0.32}
{'loss': 0.1233, 'grad_norm': 0.1371745616197586, 'learning_rate': 3.393446966351674e-05, 'epoch': 0.32}
{'loss': 0.1004, 'grad_norm': 0.2944341003894806, 'learning_rate': 3.384615384615385e-05, 'epoch': 0.32}
{'loss': 0.1089, 'grad_norm': 0.15302017331123352, 'learning_rate': 3.375872118696459e-05, 'epoch': 0.33}
{'loss': 0.1157, 'grad_norm': 0.24283944070339203, 'learning_rate': 3.36704053696017e-05, 'epoch': 0.33}
{'loss': 0.1053, 'grad_norm': 0.12418889999389648, 'learning_rate': 3.358208955223881e-05, 'epoch': 0.33}
{'loss': 0.102, 'grad_norm': 0.1718970686197281, 'learning_rate': 3.349377373487592e-05, 'epoch': 0.33}
{'loss': 0.1075, 'grad_norm': 0.26442456245422363, 'learning_rate': 3.340545791751303e-05, 'epoch': 0.33}
{'loss': 0.0998, 'grad_norm': 0.19556866586208344, 'learning_rate': 3.331714210015014e-05, 'epoch': 0.33}
{'loss': 0.1091, 'grad_norm': 0.00014930054021533579, 'learning_rate': 3.322882628278725e-05, 'epoch': 0.34}
{'loss': 0.0866, 'grad_norm': 0.09659962356090546, 'learning_rate': 3.314051046542436e-05, 'epoch': 0.34}
{'loss': 0.1326, 'grad_norm': 0.19776584208011627, 'learning_rate': 3.305219464806147e-05, 'epoch': 0.34}
{'loss': 0.0983, 'grad_norm': 9.20208913157694e-05, 'learning_rate': 3.296387883069858e-05, 'epoch': 0.34}
{'loss': 0.0992, 'grad_norm': 0.2082129567861557, 'learning_rate': 3.287556301333569e-05, 'epoch': 0.34}
{'loss': 0.0932, 'grad_norm': 0.38734135031700134, 'learning_rate': 3.27872471959728e-05, 'epoch': 0.34}
{'loss': 0.0907, 'grad_norm': 0.33099380135536194, 'learning_rate': 3.269893137860991e-05, 'epoch': 0.35}
{'loss': 0.1108, 'grad_norm': 1.6729251001379453e-05, 'learning_rate': 3.261061556124702e-05, 'epoch': 0.35}
{'loss': 0.1187, 'grad_norm': 0.274646520614624, 'learning_rate': 3.252229974388413e-05, 'epoch': 0.35}
{'loss': 0.1125, 'grad_norm': 0.28271615505218506, 'learning_rate': 3.2433983926521245e-05, 'epoch': 0.35}
{'loss': 0.109, 'grad_norm': 0.00010182964615523815, 'learning_rate': 3.234566810915835e-05, 'epoch': 0.35}
{'loss': 0.1044, 'grad_norm': 9.502789907855913e-05, 'learning_rate': 3.225735229179546e-05, 'epoch': 0.36}
{'loss': 0.1033, 'grad_norm': 0.24042236804962158, 'learning_rate': 3.2169036474432574e-05, 'epoch': 0.36}
{'loss': 0.0997, 'grad_norm': 0.3134201467037201, 'learning_rate': 3.208072065706968e-05, 'epoch': 0.36}
{'loss': 0.0983, 'grad_norm': 0.18968643248081207, 'learning_rate': 3.199240483970679e-05, 'epoch': 0.36}
{'loss': 0.1193, 'grad_norm': 0.5153762102127075, 'learning_rate': 3.1904089022343904e-05, 'epoch': 0.36}
{'loss': 0.0894, 'grad_norm': 0.21966131031513214, 'learning_rate': 3.181577320498101e-05, 'epoch': 0.36}
{'loss': 0.1058, 'grad_norm': 0.17962731420993805, 'learning_rate': 3.1727457387618126e-05, 'epoch': 0.37}
{'loss': 0.1277, 'grad_norm': 0.27659592032432556, 'learning_rate': 3.1639141570255234e-05, 'epoch': 0.37}
{'loss': 0.1057, 'grad_norm': 0.39356037974357605, 'learning_rate': 3.155082575289234e-05, 'epoch': 0.37}
{'loss': 0.1167, 'grad_norm': 0.2728269696235657, 'learning_rate': 3.1462509935529456e-05, 'epoch': 0.37}
{'loss': 0.1206, 'grad_norm': 0.1408291906118393, 'learning_rate': 3.1374194118166563e-05, 'epoch': 0.37}
{'loss': 0.1385, 'grad_norm': 0.18370917439460754, 'learning_rate': 3.128587830080368e-05, 'epoch': 0.37}
{'loss': 0.1074, 'grad_norm': 0.21798217296600342, 'learning_rate': 3.1197562483440785e-05, 'epoch': 0.38}
{'loss': 0.095, 'grad_norm': 0.14769838750362396, 'learning_rate': 3.110924666607789e-05, 'epoch': 0.38}
{'loss': 0.0991, 'grad_norm': 0.2887762784957886, 'learning_rate': 3.102093084871501e-05, 'epoch': 0.38}
{'loss': 0.1076, 'grad_norm': 0.2795463800430298, 'learning_rate': 3.093261503135212e-05, 'epoch': 0.38}
{'loss': 0.1021, 'grad_norm': 0.22434835135936737, 'learning_rate': 3.084429921398922e-05, 'epoch': 0.38}
{'loss': 0.0993, 'grad_norm': 0.2112317532300949, 'learning_rate': 3.075598339662634e-05, 'epoch': 0.39}
{'loss': 0.118, 'grad_norm': 2.0559547920129262e-05, 'learning_rate': 3.066766757926345e-05, 'epoch': 0.39}
{'loss': 0.1009, 'grad_norm': 0.3682597279548645, 'learning_rate': 3.057935176190056e-05, 'epoch': 0.39}
{'loss': 0.0936, 'grad_norm': 0.15032954514026642, 'learning_rate': 3.0491035944537667e-05, 'epoch': 0.39}
{'loss': 0.0866, 'grad_norm': 0.0037238001823425293, 'learning_rate': 3.0402720127174778e-05, 'epoch': 0.39}
{'loss': 0.0849, 'grad_norm': 0.2782649099826813, 'learning_rate': 3.031440430981189e-05, 'epoch': 0.39}
{'loss': 0.1085, 'grad_norm': 0.33167585730552673, 'learning_rate': 3.0226088492449e-05, 'epoch': 0.4}
{'loss': 0.0893, 'grad_norm': 8.652958058519289e-05, 'learning_rate': 3.0137772675086107e-05, 'epoch': 0.4}
{'loss': 0.0993, 'grad_norm': 0.1543356478214264, 'learning_rate': 3.004945685772322e-05, 'epoch': 0.4}
{'loss': 0.1015, 'grad_norm': 0.38960081338882446, 'learning_rate': 2.996202419853396e-05, 'epoch': 0.4}
{'loss': 0.1071, 'grad_norm': 0.12024746835231781, 'learning_rate': 2.9873708381171067e-05, 'epoch': 0.4}
{'loss': 0.0984, 'grad_norm': 0.3759614825248718, 'learning_rate': 2.978539256380818e-05, 'epoch': 0.4}
{'loss': 0.1065, 'grad_norm': 1.9800267182290554e-05, 'learning_rate': 2.969707674644529e-05, 'epoch': 0.41}
{'loss': 0.0988, 'grad_norm': 0.28156358003616333, 'learning_rate': 2.96087609290824e-05, 'epoch': 0.41}
{'loss': 0.1004, 'grad_norm': 0.03736622631549835, 'learning_rate': 2.9520445111719508e-05, 'epoch': 0.41}
{'loss': 0.1099, 'grad_norm': 0.2240213304758072, 'learning_rate': 2.943212929435662e-05, 'epoch': 0.41}
{'loss': 0.1055, 'grad_norm': 0.18666893243789673, 'learning_rate': 2.934381347699373e-05, 'epoch': 0.41}
{'loss': 0.0995, 'grad_norm': 0.2780750095844269, 'learning_rate': 2.925549765963084e-05, 'epoch': 0.42}
{'loss': 0.109, 'grad_norm': 0.39452481269836426, 'learning_rate': 2.9167181842267955e-05, 'epoch': 0.42}
{'loss': 0.092, 'grad_norm': 0.2768974304199219, 'learning_rate': 2.907886602490506e-05, 'epoch': 0.42}
{'loss': 0.0878, 'grad_norm': 0.29408004879951477, 'learning_rate': 2.899055020754217e-05, 'epoch': 0.42}
{'loss': 0.1244, 'grad_norm': 0.09763146191835403, 'learning_rate': 2.8902234390179285e-05, 'epoch': 0.42}
{'loss': 0.1041, 'grad_norm': 0.2225169688463211, 'learning_rate': 2.8813918572816396e-05, 'epoch': 0.42}
{'loss': 0.1102, 'grad_norm': 0.09886778891086578, 'learning_rate': 2.87256027554535e-05, 'epoch': 0.43}
{'loss': 0.1089, 'grad_norm': 0.44084402918815613, 'learning_rate': 2.863728693809061e-05, 'epoch': 0.43}
{'loss': 0.0984, 'grad_norm': 0.13986100256443024, 'learning_rate': 2.8548971120727726e-05, 'epoch': 0.43}
{'loss': 0.0952, 'grad_norm': 0.16290047764778137, 'learning_rate': 2.8460655303364837e-05, 'epoch': 0.43}
{'loss': 0.0889, 'grad_norm': 0.2000061422586441, 'learning_rate': 2.837233948600194e-05, 'epoch': 0.43}
{'loss': 0.0891, 'grad_norm': 0.5004935264587402, 'learning_rate': 2.8284023668639052e-05, 'epoch': 0.43}
{'loss': 0.1098, 'grad_norm': 0.2721097767353058, 'learning_rate': 2.8195707851276167e-05, 'epoch': 0.44}
{'loss': 0.0895, 'grad_norm': inf, 'learning_rate': 2.8107392033913278e-05, 'epoch': 0.44}
{'loss': 0.0996, 'grad_norm': 0.13388651609420776, 'learning_rate': 2.8019959374724015e-05, 'epoch': 0.44}
{'loss': 0.0942, 'grad_norm': 0.11804010719060898, 'learning_rate': 2.7931643557361126e-05, 'epoch': 0.44}
{'loss': 0.0906, 'grad_norm': 0.15732383728027344, 'learning_rate': 2.7843327739998237e-05, 'epoch': 0.44}
{'loss': 0.091, 'grad_norm': 0.2821621000766754, 'learning_rate': 2.7755011922635342e-05, 'epoch': 0.45}
{'loss': 0.1094, 'grad_norm': 0.25134846568107605, 'learning_rate': 2.7667579263446086e-05, 'epoch': 0.45}
{'loss': 0.1154, 'grad_norm': 0.3602365255355835, 'learning_rate': 2.757926344608319e-05, 'epoch': 0.45}
{'loss': 0.1193, 'grad_norm': 0.4040113389492035, 'learning_rate': 2.7490947628720305e-05, 'epoch': 0.45}
{'loss': 0.0976, 'grad_norm': 0.30261728167533875, 'learning_rate': 2.7402631811357416e-05, 'epoch': 0.45}
{'loss': 0.1121, 'grad_norm': 0.09862932562828064, 'learning_rate': 2.7314315993994527e-05, 'epoch': 0.45}
{'loss': 0.1113, 'grad_norm': 0.12598730623722076, 'learning_rate': 2.7226000176631638e-05, 'epoch': 0.46}
{'loss': 0.0754, 'grad_norm': 0.02803138457238674, 'learning_rate': 2.7137684359268746e-05, 'epoch': 0.46}
{'loss': 0.0955, 'grad_norm': 0.22000271081924438, 'learning_rate': 2.7049368541905857e-05, 'epoch': 0.46}
{'loss': 0.0964, 'grad_norm': 0.15417097508907318, 'learning_rate': 2.6961052724542968e-05, 'epoch': 0.46}
{'loss': 0.1081, 'grad_norm': 0.2786409854888916, 'learning_rate': 2.687273690718008e-05, 'epoch': 0.46}
{'loss': 0.0949, 'grad_norm': 0.22332578897476196, 'learning_rate': 2.6784421089817186e-05, 'epoch': 0.46}
{'loss': 0.1014, 'grad_norm': 0.3697570562362671, 'learning_rate': 2.6696105272454297e-05, 'epoch': 0.47}
{'loss': 0.1017, 'grad_norm': 0.1973237842321396, 'learning_rate': 2.660778945509141e-05, 'epoch': 0.47}
{'loss': 0.1171, 'grad_norm': 0.21746450662612915, 'learning_rate': 2.651947363772852e-05, 'epoch': 0.47}
{'loss': 0.1125, 'grad_norm': 0.3766867518424988, 'learning_rate': 2.6431157820365627e-05, 'epoch': 0.47}
{'loss': 0.1134, 'grad_norm': 0.16190984845161438, 'learning_rate': 2.6342842003002738e-05, 'epoch': 0.47}
{'loss': 0.1013, 'grad_norm': 0.2020818144083023, 'learning_rate': 2.625540934381348e-05, 'epoch': 0.48}
{'loss': 0.1036, 'grad_norm': 0.1889829933643341, 'learning_rate': 2.6167093526450587e-05, 'epoch': 0.48}
{'loss': 0.1258, 'grad_norm': 0.34608209133148193, 'learning_rate': 2.6078777709087698e-05, 'epoch': 0.48}
{'loss': 0.108, 'grad_norm': 0.15633311867713928, 'learning_rate': 2.599046189172481e-05, 'epoch': 0.48}
{'loss': 0.0866, 'grad_norm': 0.10655568540096283, 'learning_rate': 2.590214607436192e-05, 'epoch': 0.48}
{'loss': 0.0976, 'grad_norm': 0.12680399417877197, 'learning_rate': 2.5813830256999028e-05, 'epoch': 0.48}
{'loss': 0.1139, 'grad_norm': 0.1973254382610321, 'learning_rate': 2.572551443963614e-05, 'epoch': 0.49}
{'loss': 0.1195, 'grad_norm': 0.30552637577056885, 'learning_rate': 2.563719862227325e-05, 'epoch': 0.49}
{'loss': 0.113, 'grad_norm': 0.0905790850520134, 'learning_rate': 2.554888280491036e-05, 'epoch': 0.49}
{'loss': 0.1058, 'grad_norm': 0.294720321893692, 'learning_rate': 2.546056698754747e-05, 'epoch': 0.49}
{'loss': 0.105, 'grad_norm': 0.06934008002281189, 'learning_rate': 2.537225117018458e-05, 'epoch': 0.49}
{'loss': 0.0971, 'grad_norm': 0.307597279548645, 'learning_rate': 2.528393535282169e-05, 'epoch': 0.49}
{'loss': 0.1183, 'grad_norm': 0.05145594850182533, 'learning_rate': 2.5195619535458805e-05, 'epoch': 0.5}
{'loss': 0.1066, 'grad_norm': 0.4313318133354187, 'learning_rate': 2.5107303718095916e-05, 'epoch': 0.5}
{'loss': 0.1054, 'grad_norm': 0.17636287212371826, 'learning_rate': 2.501898790073302e-05, 'epoch': 0.5}
{'loss': 0.0953, 'grad_norm': 0.4756193161010742, 'learning_rate': 2.493067208337013e-05, 'epoch': 0.5}
{'loss': 0.1052, 'grad_norm': 0.48568370938301086, 'learning_rate': 2.4842356266007245e-05, 'epoch': 0.5}
{'loss': 0.107, 'grad_norm': 0.33709728717803955, 'learning_rate': 2.4754040448644353e-05, 'epoch': 0.51}
{'loss': 0.1075, 'grad_norm': 0.1807830035686493, 'learning_rate': 2.4665724631281464e-05, 'epoch': 0.51}
{'loss': 0.1, 'grad_norm': 0.1976647973060608, 'learning_rate': 2.4577408813918572e-05, 'epoch': 0.51}
{'loss': 0.1056, 'grad_norm': 0.4886866509914398, 'learning_rate': 2.4489092996555686e-05, 'epoch': 0.51}
{'loss': 0.1005, 'grad_norm': 1.068301796913147, 'learning_rate': 2.4400777179192794e-05, 'epoch': 0.51}
{'loss': 0.111, 'grad_norm': 0.16254378855228424, 'learning_rate': 2.4312461361829905e-05, 'epoch': 0.51}
{'loss': 0.0899, 'grad_norm': 0.07605256885290146, 'learning_rate': 2.4224145544467012e-05, 'epoch': 0.52}
{'loss': 0.1075, 'grad_norm': 0.1447412073612213, 'learning_rate': 2.4135829727104127e-05, 'epoch': 0.52}
{'loss': 0.117, 'grad_norm': 0.3028292655944824, 'learning_rate': 2.4047513909741238e-05, 'epoch': 0.52}
{'loss': 0.1181, 'grad_norm': 0.10661882162094116, 'learning_rate': 2.3959198092378345e-05, 'epoch': 0.52}
{'loss': 0.0997, 'grad_norm': 0.18006691336631775, 'learning_rate': 2.3870882275015456e-05, 'epoch': 0.52}
{'loss': 0.0943, 'grad_norm': 0.5074933767318726, 'learning_rate': 2.3782566457652567e-05, 'epoch': 0.52}
{'loss': 0.1092, 'grad_norm': 0.1512010395526886, 'learning_rate': 2.369425064028968e-05, 'epoch': 0.53}
{'loss': 0.1159, 'grad_norm': 0.289816290140152, 'learning_rate': 2.3605934822926786e-05, 'epoch': 0.53}
{'loss': 0.1031, 'grad_norm': 0.0002129983768099919, 'learning_rate': 2.3517619005563897e-05, 'epoch': 0.53}
{'loss': 0.0925, 'grad_norm': 0.00013348496577236801, 'learning_rate': 2.3429303188201008e-05, 'epoch': 0.53}
{'loss': 0.1012, 'grad_norm': 0.33413419127464294, 'learning_rate': 2.334098737083812e-05, 'epoch': 0.53}
{'loss': 0.0941, 'grad_norm': 0.16011972725391388, 'learning_rate': 2.3252671553475227e-05, 'epoch': 0.54}
{'loss': 0.0917, 'grad_norm': 0.28300046920776367, 'learning_rate': 2.3164355736112338e-05, 'epoch': 0.54}
{'loss': 0.1088, 'grad_norm': 0.16582156717777252, 'learning_rate': 2.307603991874945e-05, 'epoch': 0.54}
{'loss': 0.0838, 'grad_norm': 0.4368206560611725, 'learning_rate': 2.298772410138656e-05, 'epoch': 0.54}
{'loss': 0.1223, 'grad_norm': 0.2363627851009369, 'learning_rate': 2.2899408284023667e-05, 'epoch': 0.54}
{'loss': 0.106, 'grad_norm': 0.2214743196964264, 'learning_rate': 2.281109246666078e-05, 'epoch': 0.54}
{'loss': 0.1023, 'grad_norm': 0.08503402024507523, 'learning_rate': 2.2722776649297893e-05, 'epoch': 0.55}
{'loss': 0.1177, 'grad_norm': 0.18490979075431824, 'learning_rate': 2.2634460831935e-05, 'epoch': 0.55}
{'loss': 0.0974, 'grad_norm': 0.2317056804895401, 'learning_rate': 2.2547028172745742e-05, 'epoch': 0.55}
{'loss': 0.1097, 'grad_norm': 0.23565641045570374, 'learning_rate': 2.245871235538285e-05, 'epoch': 0.55}
{'loss': 0.0963, 'grad_norm': 0.15655915439128876, 'learning_rate': 2.237039653801996e-05, 'epoch': 0.55}
{'loss': 0.0833, 'grad_norm': 0.2723741829395294, 'learning_rate': 2.228208072065707e-05, 'epoch': 0.55}
{'loss': 0.1149, 'grad_norm': 7.211508636828512e-05, 'learning_rate': 2.2193764903294182e-05, 'epoch': 0.56}
{'loss': 0.1094, 'grad_norm': 0.08532150834798813, 'learning_rate': 2.210544908593129e-05, 'epoch': 0.56}
{'loss': 0.1071, 'grad_norm': 0.3585645854473114, 'learning_rate': 2.20171332685684e-05, 'epoch': 0.56}
{'loss': 0.0924, 'grad_norm': 0.2763226330280304, 'learning_rate': 2.1928817451205512e-05, 'epoch': 0.56}
{'loss': 0.0866, 'grad_norm': 0.3079270124435425, 'learning_rate': 2.1840501633842623e-05, 'epoch': 0.56}
{'loss': 0.0988, 'grad_norm': 0.21688050031661987, 'learning_rate': 2.1752185816479734e-05, 'epoch': 0.57}
{'loss': 0.1008, 'grad_norm': 0.3679869472980499, 'learning_rate': 2.1663869999116842e-05, 'epoch': 0.57}
{'loss': 0.1013, 'grad_norm': 0.1153392419219017, 'learning_rate': 2.1575554181753953e-05, 'epoch': 0.57}
{'loss': 0.0934, 'grad_norm': 0.12673941254615784, 'learning_rate': 2.1487238364391064e-05, 'epoch': 0.57}
{'loss': 0.0985, 'grad_norm': 0.04595246538519859, 'learning_rate': 2.1398922547028175e-05, 'epoch': 0.57}
{'loss': 0.0901, 'grad_norm': 0.2108875811100006, 'learning_rate': 2.1310606729665282e-05, 'epoch': 0.57}
{'loss': 0.1086, 'grad_norm': 0.2865687608718872, 'learning_rate': 2.1222290912302393e-05, 'epoch': 0.58}
{'loss': 0.1005, 'grad_norm': 0.3044658899307251, 'learning_rate': 2.1133975094939504e-05, 'epoch': 0.58}
{'loss': 0.1041, 'grad_norm': 0.10254466533660889, 'learning_rate': 2.1045659277576615e-05, 'epoch': 0.58}
{'loss': 0.1092, 'grad_norm': 0.17463093996047974, 'learning_rate': 2.0957343460213723e-05, 'epoch': 0.58}
{'loss': 0.114, 'grad_norm': 0.13106796145439148, 'learning_rate': 2.0869027642850834e-05, 'epoch': 0.58}
{'loss': 0.1063, 'grad_norm': 0.23366983234882355, 'learning_rate': 2.0780711825487945e-05, 'epoch': 0.58}
{'loss': 0.089, 'grad_norm': 0.34055295586586, 'learning_rate': 2.0692396008125056e-05, 'epoch': 0.59}
{'loss': 0.0999, 'grad_norm': 0.2900679111480713, 'learning_rate': 2.0604080190762167e-05, 'epoch': 0.59}
{'loss': 0.1062, 'grad_norm': 0.2863345146179199, 'learning_rate': 2.0515764373399278e-05, 'epoch': 0.59}
{'loss': 0.0837, 'grad_norm': 0.1294298768043518, 'learning_rate': 2.042744855603639e-05, 'epoch': 0.59}
{'loss': 0.1065, 'grad_norm': 0.3895430266857147, 'learning_rate': 2.0339132738673497e-05, 'epoch': 0.59}
{'loss': 0.0954, 'grad_norm': 0.2239711731672287, 'learning_rate': 2.0250816921310608e-05, 'epoch': 0.6}
{'loss': 0.1055, 'grad_norm': 0.3759722411632538, 'learning_rate': 2.016250110394772e-05, 'epoch': 0.6}
{'loss': 0.1099, 'grad_norm': 7.305704639293253e-05, 'learning_rate': 2.007418528658483e-05, 'epoch': 0.6}
{'loss': 0.1004, 'grad_norm': 0.3966688811779022, 'learning_rate': 1.9985869469221938e-05, 'epoch': 0.6}
{'loss': 0.0906, 'grad_norm': 0.2071523815393448, 'learning_rate': 1.989755365185905e-05, 'epoch': 0.6}
{'loss': 0.0956, 'grad_norm': 0.15484575927257538, 'learning_rate': 1.980923783449616e-05, 'epoch': 0.6}
{'loss': 0.1114, 'grad_norm': 0.3211897313594818, 'learning_rate': 1.972092201713327e-05, 'epoch': 0.61}
{'loss': 0.0895, 'grad_norm': 0.2841333746910095, 'learning_rate': 1.9632606199770378e-05, 'epoch': 0.61}
{'loss': 0.0904, 'grad_norm': 0.20216874778270721, 'learning_rate': 1.954429038240749e-05, 'epoch': 0.61}
{'loss': 0.0776, 'grad_norm': 0.16505169868469238, 'learning_rate': 1.94559745650446e-05, 'epoch': 0.61}
{'loss': 0.0918, 'grad_norm': 0.09024073928594589, 'learning_rate': 1.936765874768171e-05, 'epoch': 0.61}
{'loss': 0.0968, 'grad_norm': 7.364751218119636e-05, 'learning_rate': 1.9279342930318822e-05, 'epoch': 0.61}
{'loss': 0.0937, 'grad_norm': 0.0985642820596695, 'learning_rate': 1.919102711295593e-05, 'epoch': 0.62}
{'loss': 0.0802, 'grad_norm': 0.3054969608783722, 'learning_rate': 1.9102711295593044e-05, 'epoch': 0.62}
{'loss': 0.0991, 'grad_norm': 0.19140610098838806, 'learning_rate': 1.9014395478230152e-05, 'epoch': 0.62}
{'loss': 0.1039, 'grad_norm': 0.08326957374811172, 'learning_rate': 1.8926079660867263e-05, 'epoch': 0.62}
{'loss': 0.1143, 'grad_norm': 0.30122825503349304, 'learning_rate': 1.883776384350437e-05, 'epoch': 0.62}
{'loss': 0.1048, 'grad_norm': 0.3009762465953827, 'learning_rate': 1.8749448026141485e-05, 'epoch': 0.63}
{'loss': 0.1187, 'grad_norm': 0.1516299992799759, 'learning_rate': 1.8661132208778593e-05, 'epoch': 0.63}
{'loss': 0.0993, 'grad_norm': 0.00021949561778455973, 'learning_rate': 1.8572816391415704e-05, 'epoch': 0.63}
{'loss': 0.1079, 'grad_norm': 0.04260440915822983, 'learning_rate': 1.848450057405281e-05, 'epoch': 0.63}
{'loss': 0.1204, 'grad_norm': 0.13501346111297607, 'learning_rate': 1.8396184756689926e-05, 'epoch': 0.63}
{'loss': 0.0852, 'grad_norm': 0.11898383498191833, 'learning_rate': 1.8307868939327033e-05, 'epoch': 0.63}
{'loss': 0.097, 'grad_norm': 0.15898197889328003, 'learning_rate': 1.8219553121964144e-05, 'epoch': 0.64}
{'loss': 0.083, 'grad_norm': 0.30587679147720337, 'learning_rate': 1.8131237304601255e-05, 'epoch': 0.64}
{'loss': 0.0984, 'grad_norm': 0.32006266713142395, 'learning_rate': 1.8042921487238366e-05, 'epoch': 0.64}
{'loss': 0.0897, 'grad_norm': 0.43968337774276733, 'learning_rate': 1.7954605669875477e-05, 'epoch': 0.64}
{'loss': 0.0933, 'grad_norm': 0.16634920239448547, 'learning_rate': 1.7866289852512585e-05, 'epoch': 0.64}
{'loss': 0.0923, 'grad_norm': 0.0001113517428166233, 'learning_rate': 1.7777974035149696e-05, 'epoch': 0.64}
{'loss': 0.0996, 'grad_norm': 0.20027710497379303, 'learning_rate': 1.7689658217786807e-05, 'epoch': 0.65}
{'loss': 0.1149, 'grad_norm': 0.22223252058029175, 'learning_rate': 1.7602225558597545e-05, 'epoch': 0.65}
{'loss': 0.1199, 'grad_norm': 0.24205227196216583, 'learning_rate': 1.7513909741234656e-05, 'epoch': 0.65}
{'loss': 0.0837, 'grad_norm': 0.21721771359443665, 'learning_rate': 1.7425593923871767e-05, 'epoch': 0.65}
{'loss': 0.1006, 'grad_norm': 0.18734999001026154, 'learning_rate': 1.7337278106508875e-05, 'epoch': 0.65}
{'loss': 0.0914, 'grad_norm': 0.17133213579654694, 'learning_rate': 1.7248962289145986e-05, 'epoch': 0.66}
{'loss': 0.0876, 'grad_norm': 0.23534435033798218, 'learning_rate': 1.71606464717831e-05, 'epoch': 0.66}
{'loss': 0.114, 'grad_norm': 0.4018617868423462, 'learning_rate': 1.7072330654420208e-05, 'epoch': 0.66}
{'loss': 0.1011, 'grad_norm': 0.44780054688453674, 'learning_rate': 1.698401483705732e-05, 'epoch': 0.66}
{'loss': 0.1191, 'grad_norm': 0.15954868495464325, 'learning_rate': 1.6895699019694426e-05, 'epoch': 0.66}
{'loss': 0.0961, 'grad_norm': 0.051118381321430206, 'learning_rate': 1.680738320233154e-05, 'epoch': 0.66}
{'loss': 0.0926, 'grad_norm': 0.17753051221370697, 'learning_rate': 1.6719067384968648e-05, 'epoch': 0.67}
{'loss': 0.1193, 'grad_norm': 0.3301735520362854, 'learning_rate': 1.663075156760576e-05, 'epoch': 0.67}
{'loss': 0.1212, 'grad_norm': 0.4054725766181946, 'learning_rate': 1.6542435750242867e-05, 'epoch': 0.67}
{'loss': 0.0909, 'grad_norm': 0.23793788254261017, 'learning_rate': 1.645411993287998e-05, 'epoch': 0.67}
{'loss': 0.104, 'grad_norm': 0.20922328531742096, 'learning_rate': 1.636580411551709e-05, 'epoch': 0.67}
{'loss': 0.1111, 'grad_norm': 0.38419950008392334, 'learning_rate': 1.62774882981542e-05, 'epoch': 0.67}
{'loss': 0.1221, 'grad_norm': 0.23313471674919128, 'learning_rate': 1.6189172480791308e-05, 'epoch': 0.68}
{'loss': 0.0949, 'grad_norm': 0.2529100775718689, 'learning_rate': 1.6100856663428422e-05, 'epoch': 0.68}
{'loss': 0.0901, 'grad_norm': 0.2326355129480362, 'learning_rate': 1.6012540846065533e-05, 'epoch': 0.68}
{'loss': 0.0997, 'grad_norm': 5.791596049675718e-05, 'learning_rate': 1.592422502870264e-05, 'epoch': 0.68}
{'loss': 0.0993, 'grad_norm': 0.12222452461719513, 'learning_rate': 1.583590921133975e-05, 'epoch': 0.68}
{'loss': 0.1038, 'grad_norm': 0.28050705790519714, 'learning_rate': 1.5747593393976863e-05, 'epoch': 0.69}
{'loss': 0.1016, 'grad_norm': 0.5066196918487549, 'learning_rate': 1.5659277576613974e-05, 'epoch': 0.69}
{'loss': 0.1049, 'grad_norm': 0.2503311336040497, 'learning_rate': 1.557096175925108e-05, 'epoch': 0.69}
{'loss': 0.0982, 'grad_norm': 1.4756487871636637e-05, 'learning_rate': 1.5482645941888192e-05, 'epoch': 0.69}
{'loss': 0.0937, 'grad_norm': 0.16266752779483795, 'learning_rate': 1.539521328269893e-05, 'epoch': 0.69}
{'loss': 0.1059, 'grad_norm': 0.13169611990451813, 'learning_rate': 1.530689746533604e-05, 'epoch': 0.69}
{'loss': 0.0981, 'grad_norm': 0.3132759630680084, 'learning_rate': 1.521858164797315e-05, 'epoch': 0.7}
{'loss': 0.1021, 'grad_norm': 0.37600070238113403, 'learning_rate': 1.5130265830610263e-05, 'epoch': 0.7}
{'loss': 0.0959, 'grad_norm': 0.19790604710578918, 'learning_rate': 1.5041950013247374e-05, 'epoch': 0.7}
{'loss': 0.0956, 'grad_norm': 0.39556875824928284, 'learning_rate': 1.4953634195884484e-05, 'epoch': 0.7}
{'loss': 0.1032, 'grad_norm': 5.049769242759794e-05, 'learning_rate': 1.4865318378521595e-05, 'epoch': 0.7}
{'loss': 0.1057, 'grad_norm': 0.09238922595977783, 'learning_rate': 1.4777002561158704e-05, 'epoch': 0.7}
{'loss': 0.0924, 'grad_norm': 0.00016034964937716722, 'learning_rate': 1.4688686743795815e-05, 'epoch': 0.71}
{'loss': 0.0818, 'grad_norm': 0.09613197296857834, 'learning_rate': 1.4600370926432924e-05, 'epoch': 0.71}
{'loss': 0.1095, 'grad_norm': 3.696191924973391e-05, 'learning_rate': 1.4512055109070035e-05, 'epoch': 0.71}
{'loss': 0.1016, 'grad_norm': 2.863890040316619e-05, 'learning_rate': 1.4423739291707145e-05, 'epoch': 0.71}
{'loss': 0.1193, 'grad_norm': 0.22593048214912415, 'learning_rate': 1.4335423474344256e-05, 'epoch': 0.71}
{'loss': 0.0854, 'grad_norm': 0.2706512212753296, 'learning_rate': 1.4247107656981365e-05, 'epoch': 0.72}
{'loss': 0.0987, 'grad_norm': 0.24390563368797302, 'learning_rate': 1.4158791839618476e-05, 'epoch': 0.72}
{'loss': 0.1021, 'grad_norm': 0.00015924729814287275, 'learning_rate': 1.4070476022255585e-05, 'epoch': 0.72}
{'loss': 0.0992, 'grad_norm': 0.1358366757631302, 'learning_rate': 1.3982160204892696e-05, 'epoch': 0.72}
{'loss': 0.0975, 'grad_norm': 0.26638492941856384, 'learning_rate': 1.3893844387529809e-05, 'epoch': 0.72}
{'loss': 0.1095, 'grad_norm': 0.17347225546836853, 'learning_rate': 1.3805528570166917e-05, 'epoch': 0.72}
{'loss': 0.0948, 'grad_norm': 0.07408624142408371, 'learning_rate': 1.371721275280403e-05, 'epoch': 0.73}
{'loss': 0.093, 'grad_norm': 0.15355350077152252, 'learning_rate': 1.3628896935441137e-05, 'epoch': 0.73}
{'loss': 0.1087, 'grad_norm': 0.1791030615568161, 'learning_rate': 1.354058111807825e-05, 'epoch': 0.73}
{'loss': 0.1144, 'grad_norm': 0.3333481550216675, 'learning_rate': 1.3452265300715359e-05, 'epoch': 0.73}
{'loss': 0.1152, 'grad_norm': 0.34586721658706665, 'learning_rate': 1.336394948335247e-05, 'epoch': 0.73}
{'loss': 0.0989, 'grad_norm': 0.3923572897911072, 'learning_rate': 1.327563366598958e-05, 'epoch': 0.73}
{'loss': 0.1208, 'grad_norm': 0.4877377450466156, 'learning_rate': 1.318731784862669e-05, 'epoch': 0.74}
{'loss': 0.0918, 'grad_norm': 0.1759977489709854, 'learning_rate': 1.30990020312638e-05, 'epoch': 0.74}
{'loss': 0.1076, 'grad_norm': 0.20471541583538055, 'learning_rate': 1.301156937207454e-05, 'epoch': 0.74}
{'loss': 0.0978, 'grad_norm': 0.1769181787967682, 'learning_rate': 1.292325355471165e-05, 'epoch': 0.74}
{'loss': 0.111, 'grad_norm': 0.40400272607803345, 'learning_rate': 1.283493773734876e-05, 'epoch': 0.74}
{'loss': 0.1168, 'grad_norm': 0.4391617774963379, 'learning_rate': 1.274662191998587e-05, 'epoch': 0.75}
{'loss': 0.0894, 'grad_norm': 0.00010067460243590176, 'learning_rate': 1.265830610262298e-05, 'epoch': 0.75}
{'loss': 0.0774, 'grad_norm': 0.09780783206224442, 'learning_rate': 1.2569990285260091e-05, 'epoch': 0.75}
{'loss': 0.0918, 'grad_norm': 0.15572917461395264, 'learning_rate': 1.24816744678972e-05, 'epoch': 0.75}
{'loss': 0.0973, 'grad_norm': 0.28379321098327637, 'learning_rate': 1.2393358650534311e-05, 'epoch': 0.75}
{'loss': 0.0909, 'grad_norm': 5.220024104346521e-05, 'learning_rate': 1.2305042833171422e-05, 'epoch': 0.75}
{'loss': 0.1002, 'grad_norm': 0.01851475052535534, 'learning_rate': 1.2216727015808532e-05, 'epoch': 0.76}
{'loss': 0.1115, 'grad_norm': 0.12085778266191483, 'learning_rate': 1.2128411198445643e-05, 'epoch': 0.76}
{'loss': 0.1047, 'grad_norm': 0.04111051186919212, 'learning_rate': 1.2040095381082752e-05, 'epoch': 0.76}
{'loss': 0.1033, 'grad_norm': 0.43110963702201843, 'learning_rate': 1.1951779563719863e-05, 'epoch': 0.76}
{'loss': 0.1036, 'grad_norm': 0.3628581762313843, 'learning_rate': 1.1863463746356972e-05, 'epoch': 0.76}
{'loss': 0.1081, 'grad_norm': 0.22470547258853912, 'learning_rate': 1.1775147928994083e-05, 'epoch': 0.76}
{'loss': 0.0903, 'grad_norm': 0.17320138216018677, 'learning_rate': 1.1687715269804821e-05, 'epoch': 0.77}
{'loss': 0.0939, 'grad_norm': 0.4975874722003937, 'learning_rate': 1.1599399452441932e-05, 'epoch': 0.77}
{'loss': 0.0865, 'grad_norm': 0.22608108818531036, 'learning_rate': 1.1511083635079043e-05, 'epoch': 0.77}
{'loss': 0.0895, 'grad_norm': 0.17617785930633545, 'learning_rate': 1.1422767817716154e-05, 'epoch': 0.77}
{'loss': 0.098, 'grad_norm': 0.27451494336128235, 'learning_rate': 1.1334452000353264e-05, 'epoch': 0.77}
{'loss': 0.0814, 'grad_norm': 0.1393471509218216, 'learning_rate': 1.1246136182990375e-05, 'epoch': 0.78}
{'loss': 0.0837, 'grad_norm': 8.810491272015497e-05, 'learning_rate': 1.1157820365627484e-05, 'epoch': 0.78}
{'loss': 0.1024, 'grad_norm': 0.20617090165615082, 'learning_rate': 1.1069504548264595e-05, 'epoch': 0.78}
{'loss': 0.0839, 'grad_norm': 0.31176209449768066, 'learning_rate': 1.0981188730901704e-05, 'epoch': 0.78}
{'loss': 0.0974, 'grad_norm': 0.17163477838039398, 'learning_rate': 1.0892872913538815e-05, 'epoch': 0.78}
{'loss': 0.0913, 'grad_norm': 0.52289879322052, 'learning_rate': 1.0804557096175925e-05, 'epoch': 0.78}
{'loss': 0.1034, 'grad_norm': 0.07742627710103989, 'learning_rate': 1.0716241278813036e-05, 'epoch': 0.79}
{'loss': 0.0879, 'grad_norm': 0.17835941910743713, 'learning_rate': 1.0627925461450147e-05, 'epoch': 0.79}
{'loss': 0.1066, 'grad_norm': 0.34414422512054443, 'learning_rate': 1.0539609644087256e-05, 'epoch': 0.79}
{'loss': 0.0976, 'grad_norm': 0.3297159671783447, 'learning_rate': 1.0451293826724367e-05, 'epoch': 0.79}
{'loss': 0.1042, 'grad_norm': 0.18942242860794067, 'learning_rate': 1.0362978009361476e-05, 'epoch': 0.79}
{'loss': 0.1053, 'grad_norm': 0.259927898645401, 'learning_rate': 1.0274662191998587e-05, 'epoch': 0.79}
{'loss': 0.0828, 'grad_norm': 0.1301417499780655, 'learning_rate': 1.0186346374635698e-05, 'epoch': 0.8}
{'loss': 0.0895, 'grad_norm': 0.2619855999946594, 'learning_rate': 1.0098030557272808e-05, 'epoch': 0.8}
{'loss': 0.0871, 'grad_norm': 0.18525782227516174, 'learning_rate': 1.0009714739909919e-05, 'epoch': 0.8}
{'loss': 0.0942, 'grad_norm': 0.3165123462677002, 'learning_rate': 9.92139892254703e-06, 'epoch': 0.8}
{'loss': 0.0908, 'grad_norm': 0.4058592915534973, 'learning_rate': 9.833083105184139e-06, 'epoch': 0.8}
{'loss': 0.0857, 'grad_norm': 0.4179963171482086, 'learning_rate': 9.74476728782125e-06, 'epoch': 0.81}
{'loss': 0.1068, 'grad_norm': 0.17987999320030212, 'learning_rate': 9.65645147045836e-06, 'epoch': 0.81}
{'loss': 0.1053, 'grad_norm': 0.12986764311790466, 'learning_rate': 9.56813565309547e-06, 'epoch': 0.81}
{'loss': 0.1116, 'grad_norm': 0.12435925006866455, 'learning_rate': 9.47981983573258e-06, 'epoch': 0.81}
{'loss': 0.0976, 'grad_norm': 0.38154324889183044, 'learning_rate': 9.39150401836969e-06, 'epoch': 0.81}
{'loss': 0.094, 'grad_norm': 0.1969846785068512, 'learning_rate': 9.3031882010068e-06, 'epoch': 0.81}
{'loss': 0.0884, 'grad_norm': 0.11704149842262268, 'learning_rate': 9.214872383643911e-06, 'epoch': 0.82}
{'loss': 0.0844, 'grad_norm': 0.17894013226032257, 'learning_rate': 9.12655656628102e-06, 'epoch': 0.82}
{'loss': 0.113, 'grad_norm': 0.2843310832977295, 'learning_rate': 9.038240748918133e-06, 'epoch': 0.82}
{'loss': 0.1001, 'grad_norm': 0.30984005331993103, 'learning_rate': 8.949924931555242e-06, 'epoch': 0.82}
{'loss': 0.1223, 'grad_norm': 0.358766108751297, 'learning_rate': 8.861609114192353e-06, 'epoch': 0.82}
{'loss': 0.0946, 'grad_norm': 0.32327619194984436, 'learning_rate': 8.773293296829463e-06, 'epoch': 0.82}
{'loss': 0.091, 'grad_norm': 0.20210324227809906, 'learning_rate': 8.684977479466574e-06, 'epoch': 0.83}
{'loss': 0.0892, 'grad_norm': 0.3888038098812103, 'learning_rate': 8.596661662103683e-06, 'epoch': 0.83}
{'loss': 0.099, 'grad_norm': 0.18193377554416656, 'learning_rate': 8.508345844740794e-06, 'epoch': 0.83}
{'loss': 0.0951, 'grad_norm': 0.40348851680755615, 'learning_rate': 8.420030027377903e-06, 'epoch': 0.83}
{'loss': 0.1107, 'grad_norm': 0.35088714957237244, 'learning_rate': 8.331714210015014e-06, 'epoch': 0.83}
{'loss': 0.085, 'grad_norm': 0.451360285282135, 'learning_rate': 8.243398392652124e-06, 'epoch': 0.84}
{'loss': 0.1014, 'grad_norm': 0.2322586625814438, 'learning_rate': 8.155082575289235e-06, 'epoch': 0.84}
{'loss': 0.0954, 'grad_norm': 0.3254716992378235, 'learning_rate': 8.066766757926344e-06, 'epoch': 0.84}
{'loss': 0.0896, 'grad_norm': 0.30068865418434143, 'learning_rate': 7.978450940563455e-06, 'epoch': 0.84}
{'loss': 0.0966, 'grad_norm': 0.24135446548461914, 'learning_rate': 7.890135123200564e-06, 'epoch': 0.84}
{'loss': 0.0908, 'grad_norm': 0.30480292439460754, 'learning_rate': 7.802702464011306e-06, 'epoch': 0.84}
{'loss': 0.0889, 'grad_norm': 0.3220512270927429, 'learning_rate': 7.714386646648415e-06, 'epoch': 0.85}
{'loss': 0.0848, 'grad_norm': 3.830597779597156e-05, 'learning_rate': 7.626070829285525e-06, 'epoch': 0.85}
{'loss': 0.1055, 'grad_norm': 0.07983779907226562, 'learning_rate': 7.537755011922635e-06, 'epoch': 0.85}
{'loss': 0.0844, 'grad_norm': 0.5933825373649597, 'learning_rate': 7.4494391945597455e-06, 'epoch': 0.85}
{'loss': 0.1074, 'grad_norm': 0.14905202388763428, 'learning_rate': 7.361123377196856e-06, 'epoch': 0.85}
{'loss': 0.0874, 'grad_norm': 0.00028182470123283565, 'learning_rate': 7.272807559833966e-06, 'epoch': 0.85}
{'loss': 0.0895, 'grad_norm': 1.4164291314955335e-05, 'learning_rate': 7.184491742471077e-06, 'epoch': 0.86}
{'loss': 0.1009, 'grad_norm': 0.03877485916018486, 'learning_rate': 7.096175925108187e-06, 'epoch': 0.86}
{'loss': 0.0953, 'grad_norm': 0.223951056599617, 'learning_rate': 7.007860107745297e-06, 'epoch': 0.86}
{'loss': 0.1003, 'grad_norm': 0.23944707214832306, 'learning_rate': 6.919544290382408e-06, 'epoch': 0.86}
{'loss': 0.1088, 'grad_norm': 0.11844311654567719, 'learning_rate': 6.831228473019518e-06, 'epoch': 0.86}
{'loss': 0.105, 'grad_norm': 0.2309057116508484, 'learning_rate': 6.7429126556566285e-06, 'epoch': 0.87}
{'loss': 0.1002, 'grad_norm': 0.03930461406707764, 'learning_rate': 6.654596838293739e-06, 'epoch': 0.87}
{'loss': 0.1077, 'grad_norm': 0.10782831162214279, 'learning_rate': 6.566281020930849e-06, 'epoch': 0.87}
{'loss': 0.098, 'grad_norm': 0.3180006146430969, 'learning_rate': 6.477965203567959e-06, 'epoch': 0.87}
{'loss': 0.0892, 'grad_norm': 8.139569399645552e-05, 'learning_rate': 6.38964938620507e-06, 'epoch': 0.87}
{'loss': 0.1007, 'grad_norm': 0.28275489807128906, 'learning_rate': 6.30133356884218e-06, 'epoch': 0.87}
{'loss': 0.095, 'grad_norm': 0.5719020366668701, 'learning_rate': 6.21301775147929e-06, 'epoch': 0.88}
{'loss': 0.1067, 'grad_norm': 1.6483169794082642, 'learning_rate': 6.1247019341164006e-06, 'epoch': 0.88}
{'loss': 0.1061, 'grad_norm': 0.28622955083847046, 'learning_rate': 6.0363861167535116e-06, 'epoch': 0.88}
{'loss': 0.101, 'grad_norm': 0.20847810804843903, 'learning_rate': 5.9489534575642495e-06, 'epoch': 0.88}
{'loss': 0.1032, 'grad_norm': 0.056998033076524734, 'learning_rate': 5.86063764020136e-06, 'epoch': 0.88}
{'loss': 0.1057, 'grad_norm': 0.388095498085022, 'learning_rate': 5.772321822838471e-06, 'epoch': 0.88}
{'loss': 0.0857, 'grad_norm': 0.12474063038825989, 'learning_rate': 5.684006005475581e-06, 'epoch': 0.89}
{'loss': 0.0978, 'grad_norm': 0.3169806897640228, 'learning_rate': 5.595690188112691e-06, 'epoch': 0.89}
{'loss': 0.0984, 'grad_norm': 0.16546596586704254, 'learning_rate': 5.507374370749801e-06, 'epoch': 0.89}
{'loss': 0.1004, 'grad_norm': 0.2652837634086609, 'learning_rate': 5.419058553386912e-06, 'epoch': 0.89}
{'loss': 0.1061, 'grad_norm': 0.23589476943016052, 'learning_rate': 5.330742736024022e-06, 'epoch': 0.89}
{'loss': 0.0992, 'grad_norm': 0.1640658676624298, 'learning_rate': 5.2424269186611325e-06, 'epoch': 0.9}
{'loss': 0.098, 'grad_norm': 0.21923251450061798, 'learning_rate': 5.154111101298243e-06, 'epoch': 0.9}
{'loss': 0.0802, 'grad_norm': 0.13360127806663513, 'learning_rate': 5.065795283935353e-06, 'epoch': 0.9}
{'loss': 0.1092, 'grad_norm': 0.40614354610443115, 'learning_rate': 4.977479466572464e-06, 'epoch': 0.9}
{'loss': 0.1194, 'grad_norm': 0.29898759722709656, 'learning_rate': 4.889163649209574e-06, 'epoch': 0.9}
{'loss': 0.0853, 'grad_norm': 0.28552383184432983, 'learning_rate': 4.800847831846684e-06, 'epoch': 0.9}
{'loss': 0.0882, 'grad_norm': 0.23860670626163483, 'learning_rate': 4.712532014483794e-06, 'epoch': 0.91}
{'loss': 0.0917, 'grad_norm': 0.059692371636629105, 'learning_rate': 4.6242161971209045e-06, 'epoch': 0.91}
{'loss': 0.1093, 'grad_norm': 0.16860021650791168, 'learning_rate': 4.5359003797580156e-06, 'epoch': 0.91}
{'loss': 0.0917, 'grad_norm': 0.3089136779308319, 'learning_rate': 4.447584562395126e-06, 'epoch': 0.91}
{'loss': 0.1, 'grad_norm': 0.36836424469947815, 'learning_rate': 4.359268745032236e-06, 'epoch': 0.91}
{'loss': 0.097, 'grad_norm': 0.2302786260843277, 'learning_rate': 4.270952927669346e-06, 'epoch': 0.91}
{'loss': 0.0853, 'grad_norm': 0.1635035276412964, 'learning_rate': 4.183520268480085e-06, 'epoch': 0.92}
{'loss': 0.0928, 'grad_norm': 0.05929819121956825, 'learning_rate': 4.095204451117195e-06, 'epoch': 0.92}
{'loss': 0.094, 'grad_norm': 0.20385123789310455, 'learning_rate': 4.006888633754306e-06, 'epoch': 0.92}
{'loss': 0.114, 'grad_norm': 0.2689756751060486, 'learning_rate': 3.918572816391416e-06, 'epoch': 0.92}
{'loss': 0.0934, 'grad_norm': 0.3416338562965393, 'learning_rate': 3.830256999028526e-06, 'epoch': 0.92}
{'loss': 0.0867, 'grad_norm': 0.12701164186000824, 'learning_rate': 3.741941181665636e-06, 'epoch': 0.93}
{'loss': 0.1043, 'grad_norm': 0.022750500589609146, 'learning_rate': 3.653625364302747e-06, 'epoch': 0.93}
{'loss': 0.1101, 'grad_norm': 0.13300436735153198, 'learning_rate': 3.5653095469398573e-06, 'epoch': 0.93}
{'loss': 0.0816, 'grad_norm': 0.14650481939315796, 'learning_rate': 3.4769937295769674e-06, 'epoch': 0.93}
{'loss': 0.0893, 'grad_norm': 0.18269024789333344, 'learning_rate': 3.3886779122140776e-06, 'epoch': 0.93}
{'loss': 0.0942, 'grad_norm': 0.2868667542934418, 'learning_rate': 3.3003620948511878e-06, 'epoch': 0.93}
{'loss': 0.107, 'grad_norm': 0.3186851441860199, 'learning_rate': 3.212046277488298e-06, 'epoch': 0.94}
{'loss': 0.0999, 'grad_norm': 0.34507808089256287, 'learning_rate': 3.1237304601254085e-06, 'epoch': 0.94}
{'loss': 0.1003, 'grad_norm': 0.11920975893735886, 'learning_rate': 3.0354146427625187e-06, 'epoch': 0.94}
{'loss': 0.115, 'grad_norm': 0.23578238487243652, 'learning_rate': 2.947098825399629e-06, 'epoch': 0.94}
{'loss': 0.0947, 'grad_norm': 0.2867767810821533, 'learning_rate': 2.8587830080367395e-06, 'epoch': 0.94}
{'loss': 0.0837, 'grad_norm': 0.22468098998069763, 'learning_rate': 2.7704671906738496e-06, 'epoch': 0.94}
{'loss': 0.0923, 'grad_norm': 0.2216683328151703, 'learning_rate': 2.6821513733109602e-06, 'epoch': 0.95}
{'loss': 0.1027, 'grad_norm': 0.20105357468128204, 'learning_rate': 2.5938355559480704e-06, 'epoch': 0.95}
{'loss': 0.0906, 'grad_norm': 0.07332910597324371, 'learning_rate': 2.505519738585181e-06, 'epoch': 0.95}
{'loss': 0.0861, 'grad_norm': 0.25061535835266113, 'learning_rate': 2.417203921222291e-06, 'epoch': 0.95}
{'loss': 0.0888, 'grad_norm': 0.3462103605270386, 'learning_rate': 2.3288881038594013e-06, 'epoch': 0.95}
{'loss': 0.0961, 'grad_norm': 0.2112191766500473, 'learning_rate': 2.240572286496512e-06, 'epoch': 0.96}
{'loss': 0.097, 'grad_norm': 0.3955651819705963, 'learning_rate': 2.152256469133622e-06, 'epoch': 0.96}
{'loss': 0.0926, 'grad_norm': 0.482333779335022, 'learning_rate': 2.0639406517707322e-06, 'epoch': 0.96}
{'loss': 0.0966, 'grad_norm': 0.1846752166748047, 'learning_rate': 1.975624834407843e-06, 'epoch': 0.96}
{'loss': 0.1129, 'grad_norm': 4.4820295443059877e-05, 'learning_rate': 1.887309017044953e-06, 'epoch': 0.96}
{'loss': 0.1147, 'grad_norm': 0.09965037554502487, 'learning_rate': 1.7989931996820632e-06, 'epoch': 0.96}
{'loss': 0.0984, 'grad_norm': 0.26755622029304504, 'learning_rate': 1.7106773823191733e-06, 'epoch': 0.97}
{'loss': 0.0936, 'grad_norm': 0.14750075340270996, 'learning_rate': 1.622361564956284e-06, 'epoch': 0.97}
{'loss': 0.097, 'grad_norm': 0.3327470123767853, 'learning_rate': 1.534045747593394e-06, 'epoch': 0.97}
{'loss': 0.0994, 'grad_norm': 0.2819759249687195, 'learning_rate': 1.4457299302305045e-06, 'epoch': 0.97}
{'loss': 0.0933, 'grad_norm': 0.13601049780845642, 'learning_rate': 1.3574141128676146e-06, 'epoch': 0.97}
{'loss': 0.0899, 'grad_norm': 0.3639906346797943, 'learning_rate': 1.269098295504725e-06, 'epoch': 0.98}
{'loss': 0.1056, 'grad_norm': 0.3947022259235382, 'learning_rate': 1.1816656363154642e-06, 'epoch': 0.98}
{'loss': 0.0836, 'grad_norm': 0.0944313108921051, 'learning_rate': 1.0933498189525744e-06, 'epoch': 0.98}
{'loss': 0.1012, 'grad_norm': 0.32397839426994324, 'learning_rate': 1.0050340015896848e-06, 'epoch': 0.98}
{'loss': 0.1087, 'grad_norm': 0.12634599208831787, 'learning_rate': 9.16718184226795e-07, 'epoch': 0.98}
{'loss': 0.0991, 'grad_norm': 0.21568748354911804, 'learning_rate': 8.284023668639054e-07, 'epoch': 0.98}
{'loss': 0.0984, 'grad_norm': 0.18431468307971954, 'learning_rate': 7.400865495010157e-07, 'epoch': 0.99}
{'loss': 0.0775, 'grad_norm': 0.25949132442474365, 'learning_rate': 6.51770732138126e-07, 'epoch': 0.99}
{'loss': 0.1031, 'grad_norm': 0.21861274540424347, 'learning_rate': 5.634549147752362e-07, 'epoch': 0.99}
{'loss': 0.1211, 'grad_norm': 0.15446282923221588, 'learning_rate': 4.7513909741234656e-07, 'epoch': 0.99}
{'loss': 0.091, 'grad_norm': 0.1786520630121231, 'learning_rate': 3.868232800494569e-07, 'epoch': 0.99}
{'loss': 0.0901, 'grad_norm': 0.30544087290763855, 'learning_rate': 2.9850746268656716e-07, 'epoch': 0.99}
{'loss': 0.0878, 'grad_norm': 0.13242608308792114, 'learning_rate': 2.1019164532367748e-07, 'epoch': 1.0}
{'loss': 0.106, 'grad_norm': 0.28623488545417786, 'learning_rate': 1.2187582796078778e-07, 'epoch': 1.0}
{'loss': 0.0836, 'grad_norm': 0.19938541948795319, 'learning_rate': 3.3560010597898085e-08, 'epoch': 1.0}
{'train_runtime': 8078.2365, 'train_samples_per_second': 14.017, 'train_steps_per_second': 7.008, 'train_loss': 0.10706718486599584, 'epoch': 1.0}
100%|███████████████████████████████████████████████████████████████████████████| 56615/56615 [2:14:38<00:00,  7.01it/s]
(aiwork) iphartonu@RYZEN9:/mnt/c/Users/acwil/OneDrive$
