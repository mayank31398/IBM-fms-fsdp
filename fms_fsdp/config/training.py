from dataclasses import dataclass


@dataclass
class train_config:
    # model
    model_variant: str = "7b"
    ckpt_load_path: str = "/lustre/pretrain/ckpt"
    ckpt_save_path: str = "/lustre/pretrain/ckpt"

    # dataset and dataloader
    use_dummy_dataset: bool = False
    data_path: str = "/lustre/data"
    seq_length: int = 4096
    sep_token: int = 1
    datasets: str = "lang=en/dataset=commoncrawl,lang=en/dataset=webhose,lang=en/dataset=github_clean,lang=de/dataset=wikipedia,lang=es/dataset=wikipedia,lang=fr/dataset=wikipedia,lang=ja/dataset=wikipedia,lang=pt/dataset=wikipedia,lang=en/dataset=wikimedia,lang=en/dataset=uspto,lang=en/dataset=pubmedcentral,lang=en/dataset=arxiv,lang=en/dataset=stackexchange,lang=en/dataset=PG19"
    weights: str = "7700,500,550,28,17,22,25,8,100,500,175,250,100,25"
    logical_shards: int = 768

    # fsdp policies
    mixed_precision: bool = True
    fsdp_activation_checkpointing: bool = False
    selective_checkpointing: int = 1
    sharding_strategy: str = "hsdp"
    low_cpu_fsdp: bool = False

    # training spec
    seed: int = 2023
    batch_size: int = 2
    num_steps: int = 2000000
    learning_rate: float = 3e-4
    grad_clip_thresh: float = 1.0

    # profiling and logging
    use_profiler: bool = False
    use_wandb: bool = False
    wandb_dir: str = "/lustre/lchu/fms-fsdp"
    wandb_project_name = f"llama-{model_variant}"
    wandb_run_id: str = "aabbccdd"  # give a unique id per job, for resume purpose
    report_interval: int = 200
    checkpoint_interval: int = 20000

    # compile
    use_torch_compile: bool = False
