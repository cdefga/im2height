from model.train import train
from model.im2hi import IM2HI
from model.dataloader import testloader
from model.evaluate import evaluate
import torch

COLAB = False
BATCH_SIZE = 1
# PATH = '../drive/My Drive/Colab Notebooks/im2height.pt'
PATH = 'weights/im2height_augment.pt'
test_loader = testloader(colab=COLAB, batch_size=BATCH_SIZE, )

net = IM2HI()
net.load_state_dict(torch.load(PATH, map_location=torch.device('cpu')))
if torch.cuda.is_available():
    net.cuda()
criterion = torch.nn.L1Loss()
evaluate(net, test_loader, criterion=criterion)