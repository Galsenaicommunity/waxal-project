import torch
import numpy as np
import librosa


def load_audio(path, sr=16000):
    audio, sr = librosa.load(path, sr=sr)
    return audio


class Audiogmentation:
    def __init__(self, alpha=0.2, augment_audio="mix"):
        super(Audiogmentation, self).__init__()
        self.alpha = alpha
        self.augment_audio = augment_audio

    def mix(self, xi_embed):

        shuffled_index = torch.randperm(len(xi_embed))
        xb_prime = xi_embed[shuffled_index]

        p_i = self.alpha * xi_embed + (1 - self.alpha) * xb_prime
        return p_i

    def gaussian_noise(self, xi_embed):
        noise = torch.randn(len(xi_embed))
        p_i = np.concatenate((xi_embed, noise), axis=0)
        return p_i

    def __call__(self, xi_embed):

        if self.augment_audio == "mix":
            p_i = self.mix(xi_embed)
        elif self.augment_audio == "gaussian_noise":
            p_i = self.gaussian_noise(xi_embed)
        else:
            raise ValueError("Augmentation method not implemented")
        return p_i

    def __repr__(self):
        return (
            f"Audiogmentation(alpha={self.alpha}, augment_audio={self.augment_audio})"
        )


if __name__ == "__main__":

    audio = load_audio("audio.wav")
    augmen = Audiogmentation(alpha=0.2, augment_audio="gaussian_noise")
    audio = augmen(audio)
