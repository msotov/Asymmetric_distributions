from lmfit import minimize, Minimizer, Parameters
import numpy as np
from scipy.stats import skewnorm, norm
from scipy.integrate import quad

def integrand(x, mu, sigma, alpha):
    return skewnorm.pdf(x, a=alpha, loc=mu, scale=sigma)

def fnc2min(params, x, data):
    mu = params['mu']
    sigma = params['sigma']
    alpha = params['alpha']
    
    model_0 = quad(integrand, -np.inf, x[0], args=(mu, sigma, alpha))
    model_1 = quad(integrand, -np.inf, x[1], args=(mu, sigma, alpha))
    model_2 = quad(integrand, -np.inf, x[2], args=(mu, sigma, alpha))
        
    model = np.array([model_0[0], model_1[0], model_2[0]])
        
    r = np.abs(data-model)
    
    return r

def asymmetric_samples(mean, plus, minus, size = 5000):
    if (plus == 0.0) and (minus == 0.0):
        samples = np.ones(size)*mean
        return samples

    x = np.array([mean-minus, mean, mean+plus])
    data = np.array([0.16, 0.5, 0.84])
    
    params = Parameters()
    params.add('mu', value=mean)
    params.add('sigma', value=np.mean([minus, plus]))
    params.add('alpha', value=0.0)
    
    #print(params['mu'].value, params['sigma'].value, params['alpha'].value)
    
    try:
    
        minner = Minimizer(fnc2min, params, fcn_args=(x, data))
        result = minner.minimize()
    
        mu = result.params['mu'].value
        sigma = result.params['sigma'].value
        alpha = result.params['alpha'].value
    
        samples = skewnorm.rvs(a=alpha, loc=mu, scale=sigma, size=size)
    
    except ValueError:
        samples = norm.rvs(loc=mean, scale=np.mean([minus, plus]), size=size)
    
    return samples
