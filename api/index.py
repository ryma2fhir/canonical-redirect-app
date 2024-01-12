from flask import Flask, request, redirect, render_template

app = Flask(__name__)

resolve_url = "https://simplifier.net/resolve?canonical={}&scope={}"

@app.route('/')
def home():
    example_indirect_canonical = "StructureDefinition/UKCore-AllergyIntolerance"
    example_direct_canonical = "/fhir/StructureDefinition/ACME-base-patient"
    return render_template('home.html',
                           example_indirect_canonical=example_indirect_canonical,
                           example_direct_canonical=example_direct_canonical)

''' Redirects R4 version of UK Core '''
@app.route('/')
@app.route('/CapabilityStatement/<path:rest>')
@app.route('/CodeSystem/<path:rest>')
@app.route('/ConceptMap/<path:rest>')
@app.route('/StructureDefinition/<path:rest>')
@app.route('/ValueSet/<path:rest>')
def canonicalRedirectDirect(rest=None):
    canonical = str(request.url)
    scope = "hl7fhirukcorer4@current"
    redirect_url = resolve_url.format(canonical, scope)
    return redirect(redirect_url, code=301)
 
''' Redirects STU3 version of UK Core ''' 
@app.route('/')
@app.route('/STU3/<path:rest>')
def canonicalRedirectDirect(rest=None):
    canonical = str(request.url)
    scope = "careconnect.stu3.03.00.00@3.1.0"
    redirect_url = resolve_url.format(canonical, scope)
    return redirect(redirect_url, code=301)

'''
@app.route('/')
@app.route('/<path:rest>')
def canonicalRedirectIndirect(rest=None):
    canonical = str(request.url)
    scope = "hl7fhirukcorer4"
    redirect_url = resolve_url.format(canonical, scope)
    return render_template('redirect.html', redirect_url=redirect_url)
'''    

@app.route('/<path:rest>')
def Fallback(rest=None):
    return render_template('other.html')


    
