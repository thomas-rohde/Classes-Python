'''Transforma um ang em seno, cos, e tan'''
import math
ang = float(input('Insira o ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('Com o âng. {}, temos como seno {:.2f}, como cosseno {:.2f}, e a tangente {:.2f}'.format(ang, sen, cos, tan))