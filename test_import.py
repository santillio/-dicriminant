import types, sys
code = open('discriminant.py', encoding='utf-8').read()
module = types.ModuleType('discriminant')
exec(code, module.__dict__)
sys.modules['discriminant'] = module
globals()['discriminant'] = module
print(discriminant.solve(1, -3, 2))
