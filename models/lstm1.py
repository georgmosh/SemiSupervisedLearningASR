import torch.cuda
import torch.nn as nn
import torch.nn.functional as F

class LSTM(nn.Module):

    def __init__(self, mfccs, output_phonemes, size_hidden_layers, name='vanillaLSTMfullylabeled.pth'):
        super(LSTM, self).__init__()
        '''input: number of mfcc coefficients, number of output phonemes, layer dimensions in a list
                '''
        self.name = name
        self.hidden_layers = nn.LSTM(mfccs, size_hidden_layers, dropout = 0.5, num_layers = 2, batch_first= False)
        self.output_layer = nn.Linear(size_hidden_layers, output_phonemes)

    def forward(self, x):
        x, _ = self.hidden_layers(x)
        return self.output_layer(x)

