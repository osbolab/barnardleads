SELECT
  datetime(leads_call.date, 'localtime') as date,
  leads_leadtype.type as type,
  leads_lead.name as name,
  leads_lead.phone1 as phone1,
  leads_lead.phone2 as phone2,
  leads_calloutcome.outcome as outcome,
  leads_call.notes as notes
FROM leads_call
LEFT JOIN leads_lead ON leads_lead.id = leads_call.lead_id
LEFT JOIN leads_leadtype ON leads_leadtype.type = leads_lead.type_id
LEFT JOIN leads_leadstatus ON leads_leadstatus.status = leads_lead.status_id
LEFT JOIN leads_calloutcome ON leads_calloutcome.outcome = leads_call.outcome_id
WHERE NOT leads_lead.dnc
      AND leads_leadstatus.status != 'Dead'
ORDER BY date;