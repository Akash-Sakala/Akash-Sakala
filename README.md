<!--
  Akash Sakala · GitHub profile
  The animations in assets/*.webp are HTML rendered to video with HyperFrames.
  Source: profile-src/ · rebuilt by .github/workflows/render-profile-assets.yml
-->

<a href="https://github.com/Akash-Sakala"><img src="assets/hero.webp" width="100%" alt="Akash Sakala: ML engineer who trains, fine-tunes and ships models end to end" /></a>

<div align="center">

<a href="https://www.linkedin.com/in/akash-s-s/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
<a href="https://huggingface.co/Akash-Sakala"><img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black" alt="Hugging Face" /></a>
<a href="https://leetcode.com/u/Akash_SS/"><img src="https://img.shields.io/badge/LeetCode-1A1A1A?style=flat-square&logo=leetcode&logoColor=FFA116" alt="LeetCode" /></a>
<a href="mailto:akashsakala04@gmail.com"><img src="https://img.shields.io/badge/Email-131418?style=flat-square&logo=gmail&logoColor=EA4335" alt="Email" /></a>
<img src="https://komarev.com/ghpvc/?username=Akash-Sakala&style=flat-square&color=58A6FF&label=Profile+views" alt="Profile views" />

</div>

I train, fine-tune and ship models: LLM post-training and distillation, speech recognition, and vision and audio models. When a model needs a product around it, I build that too. I'm an **Associate Applications Developer at Oracle** (Java, Spring Boot). Before that, as an **AI Research Intern at Voibe**, I distilled a 120B LLM into a 4B model that kept 99.4% of the teacher's score.

<div align="center">

| **120B → 4B** | **9.16% → 4.51%** | **91.3%** | **+29 pts** |
| :---: | :---: | :---: | :---: |
| LLM distilled, 99.4% of the teacher's score, 1 GPU instead of many | Whisper word error rate on Indian English, with a 42 MB LoRA | ESC-50 sound classification (humans: 81.3%) | macro-F1 from quantum-circuit features with 64 training farms |

</div>

## Selected work

<a href="https://github.com/Akash-Sakala/AgriQNet-2.0"><img src="assets/agri.webp" width="100%" alt="AgriQNet 2.0: farm assistant with quantum-hybrid recommendations, pest alerts, a RAG library and weather alerts" /></a>

**[AgriQNet 2.0](https://github.com/Akash-Sakala/AgriQNet-2.0)**: a farm assistant for Karnataka's farmers, built solo as my capstone. Seven services start with one command and work in Kannada, Hindi, Telugu and English:

- Crop and fertilizer recommenders that add quantum-circuit features to classical models. Each one is tested against its classical twin with nested cross-validation.
- YOLOv8 names a pest from a photo, then an SMS warns farmers in nearby districts.
- A RAG library over ICAR and UAS farm books that cites the page for every answer.
- District weather alerts.

<sub>`React` `Node.js` `FastAPI` `MongoDB` `scikit-learn` `NumPy circuit simulator` `YOLOv8` `RAG`</sub>

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/Akash-Sakala/ai-podcast-clipper"><img src="assets/clipper.webp" width="100%" alt="AI Podcast Clipper: transcribe, rank moments, render 9:16 clips" /></a>
<br />
<b><a href="https://github.com/Akash-Sakala/ai-podcast-clipper">AI Podcast Clipper</a></b>: paste a YouTube link and get ranked 9:16 Shorts. The crop follows whoever is speaking, and subtitles are timed to each word. It's a local-first fork of <a href="https://github.com/Andreaswt/ai-podcast-clipper-saas">ai-podcast-clipper-saas</a> that I rebuilt around Parakeet transcription, Gemini ranking and one GPU per clip.
<br /><sub><code>Python</code> <code>Modal</code> <code>Parakeet</code> <code>Gemini</code> <code>Next.js</code></sub>
</td>
<td width="50%" valign="top">
<a href="https://github.com/Akash-Sakala/audio-cnn"><img src="assets/audiocnn.webp" width="100%" alt="Audio CNN: spectrogram, ResNet-34 feature maps, predictions" /></a>
<br />
<b><a href="https://github.com/Akash-Sakala/audio-cnn">Audio CNN</a></b>: a ResNet-34 for 50 environmental sounds. ImageNet transfer, SpecAugment and EMA took accuracy from 83.0% to 91.3%, and a GPU-resident pipeline cut training from 48 to 2.2 minutes. It runs offline on a CPU, with a dashboard of 37 layer-by-layer feature maps.
<br /><sub><code>PyTorch</code> <code>Modal</code> <code>FastAPI</code> <code>Next.js</code> · <a href="https://huggingface.co/Akash-Sakala/audio-cnn-resnet34-esc50">🤗 model</a></sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/Akash-Sakala/Kriya-AI"><img src="assets/kriya.webp" width="100%" alt="Kriya AI: five agents plan, design, code, test and debug an app" /></a>
<br />
<b><a href="https://github.com/Akash-Sakala/Kriya-AI">Kriya AI</a></b>: a CLI where five LangGraph agents turn a prompt into a working app. A tester and a debugger repair failures in a loop. It falls back to another model on errors, uses sandboxed tools, and can resume after a crash.
<br /><sub><code>LangGraph</code> <code>Groq</code> <code>Pydantic</code> <code>SQLite</code></sub>
</td>
<td width="50%" valign="top">

### 🤗 Model lab

Ten models and two datasets on [Hugging Face](https://huggingface.co/Akash-Sakala), mostly about **making models smaller without losing quality**:

- **LLM distillation**: [gpt-oss-120b](https://huggingface.co/Akash-Sakala/gpt-oss-120b-transcript-formatter-lora) → [20b](https://huggingface.co/Akash-Sakala/gpt-oss-20b-transcript-formatter-lora) → [Qwen3.5-4B](https://huggingface.co/Akash-Sakala/qwen3.5-4b-transcript-formatter-lora), 99.4% vs the teacher's 99.9%
- **Speech**: [Whisper-small LoRA](https://huggingface.co/Akash-Sakala/whisper-small-emotion) (WER 9.16% → 4.51%) and a [Whisper-large-v3 QLoRA](https://huggingface.co/Akash-Sakala/whisper-large-v3-svarah-indic) on Indian-accented English
- **Distil, then quantize**: [BERT → DistilBERT → 4-bit](https://huggingface.co/Akash-Sakala/bert-phishing-classifier_student_4bit), 4× smaller and more accurate than the teacher

<sub>[See the family trees ↓](#-model-lab-on-hugging-face)</sub>

</td>
</tr>
</table>

## Journey

<img src="assets/timeline.webp" width="100%" alt="BMS College of Engineering (CGPA 9.73) → Netradyne SDET intern → Voibe AI research intern → Oracle" />

<details>
<summary><b>Details by role</b></summary>
<br />

- **Oracle**, Associate Applications Developer (Aug 2026 to now): enterprise Java and Spring Boot.
- **Voibe**, AI Research Intern, voice AI (Jan to Jul 2026):
  - Distilled a 120B teacher into a 4B student for ASR transcript formatting, using cross-tokenizer SFT and RLVR. Serving went from a multi-GPU MoE deployment to one INT4 GPU.
  - Cut Whisper's WER on Indian English from 9.16% to 4.51% with a LoRA trained on a custom set of 6,000 clips.
  - Built a crash-safe evaluation harness and a self-hosted WhisperX + pyannote pipeline that replaced paid ASR APIs.
- **Netradyne**, SDET Intern, Analytics (May to Aug 2025):
  - Built a pySerial/Linux framework that cut IoT flashing and OTA installs from 2.5 hours to 40 minutes. Two teams (32+ engineers) use it.
  - Automated RMA lookups from about 5 minutes to under 60 seconds.
- **BMS College of Engineering**, B.E. in AI & Machine Learning, CGPA 9.73/10, class of 2026.

</details>

## 🤗 Model lab on Hugging Face

**Transcript formatting at Voibe:** a 120B teacher distilled down to a 4B student.

```mermaid
flowchart LR
    T["gpt-oss-120b<br/>teacher · SFT + RLVR<br/>99.9%"] -- distill --> M["gpt-oss-20b<br/>student"] -- cross-tokenizer<br/>distill --> S["Qwen3.5-4B<br/>INT4 · 1 GPU<br/>99.4% ✨"]
```

**Phishing URL classifier:** distil, then quantize.

```mermaid
flowchart LR
    B["BERT-base<br/>438 MB · 89.7%"] -- KD --> D["DistilBERT<br/>211 MB · 96.0%"] -- NF4 --> Q["4-bit student<br/>110 MB · 95.8% ✨"]
```

| Model | Task | Highlight |
| :--- | :--- | :--- |
| **[qwen3.5-4b-transcript-formatter-lora](https://huggingface.co/Akash-Sakala/qwen3.5-4b-transcript-formatter-lora)** | Transcript formatting | Distilled 4B student, **99.4%** vs the 120B teacher's 99.9% |
| [gpt-oss-20b](https://huggingface.co/Akash-Sakala/gpt-oss-20b-transcript-formatter-lora) · [gpt-oss-120b](https://huggingface.co/Akash-Sakala/gpt-oss-120b-transcript-formatter-lora) · [flan-t5-large](https://huggingface.co/Akash-Sakala/flan-t5-large-transcript-formatter) | Transcript formatting | Teacher, intermediate student and baseline in the same lineage |
| **[whisper-small-emotion](https://huggingface.co/Akash-Sakala/whisper-small-emotion)** | Speech recognition | LoRA for Indian-English and expressive speech: WER **9.16% → 4.51%**, 42 MB adapter |
| [whisper-large-v3-svarah-indic](https://huggingface.co/Akash-Sakala/whisper-large-v3-svarah-indic) | Speech recognition | QLoRA (4-bit NF4) on AI4Bharat's Svarah, ~1% of parameters trained |
| **[bert-phishing-classifier_student_4bit](https://huggingface.co/Akash-Sakala/bert-phishing-classifier_student_4bit)** | Text classification | Distil, then quantize: **4× smaller** than the teacher and more accurate |
| **[audio-cnn-resnet34-esc50](https://huggingface.co/Akash-Sakala/audio-cnn-resnet34-esc50)** | Audio classification | **93.25%** top-1 on a held-out fold, ~57 ms per clip on CPU |
| [phishing-site-classification](https://huggingface.co/datasets/Akash-Sakala/phishing-site-classification) · [transcript-formatter-curriculum](https://huggingface.co/datasets/Akash-Sakala/transcript-formatter-curriculum) | Datasets | The training data behind the models above |

## Toolbox

<div align="center">

<img src="https://skillicons.dev/icons?i=python,pytorch,java,ts,js,mysql&theme=dark" alt="Python, PyTorch, Java, TypeScript, JavaScript, SQL" />
<br />
<img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" height="26" alt="Hugging Face" />
<img src="https://img.shields.io/badge/LoRA%20%2F%20PEFT-58A6FF?style=for-the-badge" height="26" alt="LoRA / PEFT" />
<img src="https://img.shields.io/badge/Distillation-8957E5?style=for-the-badge" height="26" alt="Distillation" />
<img src="https://img.shields.io/badge/Quantization-1F6FEB?style=for-the-badge" height="26" alt="Quantization" />
<img src="https://img.shields.io/badge/RLVR-2EA043?style=for-the-badge" height="26" alt="RLVR" />
<img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" height="26" alt="LangGraph" />
<br />
<img src="https://skillicons.dev/icons?i=spring,fastapi,nodejs,react,nextjs,mongodb,sqlite,aws,cloudflare,docker,linux&theme=dark" alt="Spring Boot, FastAPI, Node.js, React, Next.js, MongoDB, SQLite, AWS, Cloudflare, Docker, Linux" />
<br />
<img src="https://img.shields.io/badge/Modal-62DE61?style=for-the-badge&logoColor=black" height="26" alt="Modal" />
<img src="https://img.shields.io/badge/RunPod-673AB7?style=for-the-badge" height="26" alt="RunPod" />
<img src="https://img.shields.io/badge/Tinker-30363D?style=for-the-badge" height="26" alt="Tinker" />

</div>

## Activity

<div align="center">

<img height="160" src="./profile/stats.svg" alt="GitHub stats" />
<img height="160" src="./profile/top-langs.svg" alt="Top languages" />
<br />
<img height="160" src="https://streak-stats.demolab.com/?user=Akash-Sakala&hide_border=true&background=0D1117&stroke=30363D&ring=58A6FF&fire=58A6FF&currStreakLabel=58A6FF&sideLabels=C9D1D9&dates=8B949E&currStreakNum=C9D1D9&sideNums=C9D1D9&dayLabels=8B949E&excludeDaysLabel=8B949E" alt="GitHub streak" />
<a href="https://leetcode.com/u/Akash_SS/"><img height="160" src="https://leetcard.jacoblin.cool/Akash_SS?theme=dark&font=Fira%20Code" alt="LeetCode stats" /></a>

</div>

<details>
<summary>🕹️ <b>Insert coin</b>: Pac-Man eats my contribution graph</summary>
<br />
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Akash-Sakala/Akash-Sakala/output/pacman-contribution-graph-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Akash-Sakala/Akash-Sakala/output/pacman-contribution-graph.svg" />
  <img alt="Pac-Man eating my contribution graph" src="https://raw.githubusercontent.com/Akash-Sakala/Akash-Sakala/output/pacman-contribution-graph.svg" />
</picture>
</details>

<details>
<summary>🧰 <b>More from the workshop</b>: earlier builds and learning projects</summary>
<br />

| Repo | Notes |
| :--- | :--- |
| [Edu-Streamliners](https://github.com/Akash-Sakala/Edu-streamliners) | School platform: plain-English questions over MongoDB, a Gemini lesson planner and offline attendance, shipped in Docker |
| [Chethana AI](https://github.com/Akash-Sakala/Chethana_AI) | Flask app that predicts 42 diseases from symptoms, with diet and workout plans, Mapbox clinic search and Twilio reminders |
| [AgriQNet v1](https://github.com/Akash-Sakala/AgriQNet) · [agri-rag](https://github.com/Akash-Sakala/agri-rag) · [pest_detection_yolo](https://github.com/Akash-Sakala/pest_detection_yolo) · [agro_backend](https://github.com/Akash-Sakala/agro_backend) | The first version of AgriQNet and its services, before 2.0 |
| [own-web-server](https://github.com/Akash-Sakala/own-web-server) · [PyGit](https://github.com/Akash-Sakala/PyGit) | An HTTP server and Git internals, built from scratch in Python |
| [node-email-service](https://github.com/Akash-Sakala/node-email-service) · [weather-app](https://github.com/Akash-Sakala/weather-app) · [ai-mentor-saas-app](https://github.com/Akash-Sakala/ai-mentor-saas-app) | A Nodemailer plugin, a Dockerized React weather app and a Next.js AI-mentor experiment |

</details>

---

<div align="center">

Happy to talk about distillation, speech models, or anything that runs faster than it should.<br />
<a href="https://www.linkedin.com/in/akash-s-s/">LinkedIn</a> · <a href="https://huggingface.co/Akash-Sakala">Hugging Face</a> · <a href="mailto:akashsakala04@gmail.com">akashsakala04@gmail.com</a>

<sub>The animations on this page are HTML rendered to video with <a href="https://github.com/heygen-com/hyperframes">HyperFrames</a>. Source: <a href="https://github.com/Akash-Sakala/Akash-Sakala/tree/main/profile-src">profile-src/</a></sub>

</div>
