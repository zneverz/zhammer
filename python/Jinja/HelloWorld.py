import shutil
from jinja2 import Environment, PackageLoader

domains = ['DepositCertificate', 'CreditCertificate', 'LossInfo']

Srv_destpath = '/Users/tongjia/Documents/source_base/dvloans/dvSettleDataReg/DataPatch/Services/'
Imp_destpath = '/Users/tongjia/Documents/source_base/dvloans/dvSettleDataReg/Services/'
Con_destpath = '/Users/tongjia/Documents/source_base/dvloans/dvSettleDataReg/Controllers/'

env = Environment(loader=PackageLoader('Workdir'))
# template = env.get_template('SetServiceTp.j2')
# template = env.get_template('SetHisServiceTp.j2')
# template = env.get_template('ImplTp.j2')
template = env.get_template('ControllerTp.j2')

pos = 0
final = len(domains)

while pos < final:
    content = template.render(DomainName=domains[pos])
    # filename = './Workdir/results/' + domains[pos] + 'Srv.cs'
    # filename = './Workdir/results/' + domains[pos] + 'HisSrv.cs'
    # filename = './Workdir/results/' + domains[pos] + 'Impl.cs'
    filename = './Workdir/results/' + domains[pos] + 'Controller.cs'
    with open(filename, 'w') as fp:
        fp.write(content)
    pos += 1
    # shutil.move(filename, Srv_destpath)
    # shutil.move(filename, Imp_destpath)
    shutil.move(filename, Con_destpath)

print('Generatation Finished !')
