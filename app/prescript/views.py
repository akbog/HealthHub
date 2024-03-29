from flask import render_template, redirect, request, url_for, flash
from .forms import NewPrescriptionForm
from datetime import datetime, date
from flask_login import login_user, login_required, logout_user, current_user
from ..models import Prescription, User, Permission
from .. import db
from . import prescript
from flask_jsonpify import jsonify
from ..decorators import permission_required
from flask import session
import math
import re


@prescript.route('/new_prescription', methods = ['GET','POST'])
@login_required
@permission_required(Permission.INSERT_PRESCRIPTION)
def new_prescription():
    print("form")
    form = NewPrescriptionForm()
    print(form)
    print(form.validate_on_submit())
    if form.validate_on_submit():
        #search = request.args.get('search')
        #result = User.Query(user).filter(full_name.like('%' + search + '%')).all()
        pi = session.get("Patient_ID", None)
        prescription = Prescription(
                    patient_id = pi,
                    physician_id = current_user.user_id,
                    date_prescribed = datetime.utcnow(),
                    expir_date = form.expir_date.data,
                    description = form.description.data,
                    time = math.floor(16 / form.freq.data))
        db.session.add(prescription)
        print(prescription)
        db.session.commit()
        flash('New Prescription Created.')
        #session.pop("Patient_ID")
        return redirect(url_for('profile.search'))
        #Need to figure out form formatting for where to throw each patient
    return render_template('prescript/new_prescription.html', form = form)

@prescript.route('/view_prescriptions', methods = ['GET', 'POST'])
@login_required
@permission_required(Permission.VIEW_PRESCRIPTION)
def view_prescriptions():
    active_prescriptions = Prescription.Query(patient_id = current_user.user_id).all()
    return render_template('prescript/view_prescription.html', data = active_prescriptions)

@prescript.route('/search_pre', methods = ['GET', 'POST'])
@login_required
def modify_prescrpt():
    x =1
